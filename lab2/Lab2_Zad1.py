import threading
import random
import time

# Liczba punktów do wygenerowania
total_points = 4000000

# Liczba punktów wewnątrz okręgu (zmienna współdzielona)
points_inside_circle = 0

# Zamek do synchronizacji dostępu do zmiennej współdzielonej
lock = threading.Lock()

def monte_carlo_simulation(points):
    global points_inside_circle

    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            with lock:
                points_inside_circle += 1

# Tworzenie i startowanie wątków
num_threads = 50000
threads = []

points_per_thread = total_points // num_threads

# Mierzenie czasu rozpoczęcia
start_time = time.time()

for _ in range(num_threads):
    thread = threading.Thread(target=monte_carlo_simulation, args=(points_per_thread,))
    threads.append(thread)
    thread.start()

# Oczekiwanie na zakończenie wątków
for thread in threads:
    thread.join()

# Mierzenie czasu zakończenia
end_time = time.time()

# Obliczanie wartości liczby pi
pi_approximation = 4 * points_inside_circle / total_points

# Obliczanie i wyświetlanie całkowitego czasu wykonania
total_time = end_time - start_time
print(f"Przybliżona wartość liczby pi: {pi_approximation}")
print(f"Czas wykonania: {total_time} sekund")


#Wniosek: Im wiecej watkow tym mniejsza dokladnosc dla obliczenia przyblizonej wartosci liczby pi,
# im wieksza ilosc punktow i watkow tym wyzszy czas wykonywania programu 
