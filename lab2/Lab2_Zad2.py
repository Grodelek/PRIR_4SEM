import threading
import numpy as np


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

global_sum = np.zeros((3, 3))

lock = threading.RLock()

def multiply_and_sum():
    local_sum = np.zeros((3, 3))
    for _ in range(2000):
        result = np.dot(matrix, matrix)
        local_sum += result
    with lock:
        global global_sum
        global_sum += local_sum

num_threads = 2
threads = []


for _ in range(num_threads):
    thread = threading.Thread(target=multiply_and_sum)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print(f"Ostateczna suma wyników: \n{global_sum}")
