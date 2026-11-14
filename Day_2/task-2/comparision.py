import random
import time


def bubble_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            temp = a[i]
            a[i] = a[min_idx]
            a[min_idx] = temp
    return a


def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def quick_sort(arr):
    a = list(arr)
    stack = [(0, len(a) - 1)]
    while len(stack) > 0:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        temp = a[i + 1]
        a[i + 1] = a[high]
        a[high] = temp
        p = i + 1
        stack.append((low, p - 1))
        stack.append((p + 1, high))
    return a


def heap_sort(arr):
    a = list(arr)
    n = len(a)

    def heapify(size, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and a[l] > a[largest]:
            largest = l
        if r < size and a[r] > a[largest]:
            largest = r
        if largest != i:
            temp = a[i]
            a[i] = a[largest]
            a[largest] = temp
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        heapify(i, 0)
    return a


algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

sizes = [100, 200, 500, 1000]

print("\nSORTING ALGORITHM PERFORMANCE COMPARISON")
print("=" * 80)
print("{:<18} {:<15} {:<10} {:<15}".format("Algorithm", "Input Type", "Size", "Time (seconds)"))
print("-" * 80)

for n in sizes:
    rand_data = random.sample(range(n * 10), n)
    sorted_data = sorted(rand_data)
    rev_data = sorted_data[::-1]

    inputs = {
        "Random": rand_data,
        "Sorted": sorted_data,
        "Reverse": rev_data
    }

    for name, algo in algorithms.items():
        for in_type, data in inputs.items():
            t1 = time.perf_counter()
            out = algo(data)
            t2 = time.perf_counter()
            elapsed = t2 - t1
            assert out == sorted(data)
            print("{:<18} {:<15} {:<10} {:<15.8f}".format(name, in_type, n, elapsed))
    print("-" * 80)

print("\nPerformance testing completed successfully!")

