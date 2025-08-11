import random
import time
import matplotlib.pyplot as plt
import numpy as np


# Детермінований QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Вимірювання часу
def measure_time(sort_function, arr, repeats=5):
    times = []
    for _ in range(repeats):
        copy_arr = arr.copy()
        start = time.perf_counter()
        sort_function(copy_arr)
        end = time.perf_counter()
        times.append(end - start)
    return np.mean(times)


# Вивід результату тесту
def print_results_table(size, time_rand, time_det):
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {time_rand:.4f} секунд")
    print(f"   Детермінований QuickSort: {time_det:.4f} секунд\n")

# Побудова графіка
def plot_results(sizes, results_randomized, results_deterministic):
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, results_randomized, marker="o", label="Рандомізований QuickSort")
    plt.plot(sizes, results_deterministic, marker="s", label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (сек)")
    plt.title("Порівняння швидкості QuickSort алгоритмів")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    results_randomized = []
    results_deterministic = []

    for size in sizes:
        arr = [random.randint(0, 1_000_000) for _ in range(size)]

        time_rand = measure_time(randomized_quick_sort, arr)
        time_det = measure_time(deterministic_quick_sort, arr)

        results_randomized.append(time_rand)
        results_deterministic.append(time_det)

        print_results_table(size, time_rand, time_det)

    plot_results(sizes, results_randomized, results_deterministic)