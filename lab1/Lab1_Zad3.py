import random
import threading


def add_vec(list1, list2, result, start, end):
    for i in range(start, end):
        result[i] = list1[i] + list2[i]


def multiply_vec(list1, list2, result, start, end):
    for i in range(start, end):
        result[i] = list1[i] * list2[i]

N = int(input("Podaj liczbe N elementow wektorow "))
L = int(input("Podaj liczbe watkow L:"))
if __name__ == "__main__":
    list_a = [random.randint(1, 10) for _ in range(N)]
    list_b = [random.randint(1, 10) for _ in range(N)]
    result_add = [0] * len(list_a)
    result_mul = [0] * len(list_a)

    thread_count = L
    chunk_size = len(list_a) // thread_count
    threads = []

    for i in range(thread_count):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < thread_count - 1 else len(list_a)
        thread = threading.Thread(target=add_vec, args=(list_a, list_b, result_add, start_index, end_index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    threads = []

    for i in range(thread_count):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < thread_count - 1 else len(list_a)

        thread = threading.Thread(target=multiply_vec, args=(list_a, list_b, result_mul, start_index, end_index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Wektor A: ", list_a)
    print("Wektor B: ", list_b)
    print("Result add: ", result_add)
    print("Result multiply: ", result_mul)
