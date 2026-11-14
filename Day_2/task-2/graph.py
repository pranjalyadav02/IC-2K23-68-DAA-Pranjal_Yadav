import csv
import random
import time
import matplotlib.pyplot as plt


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
    "Heap Sort": heap_sort,
}

sizes = [100, 200, 500, 1000]
results = []
random.seed(42)

for n in sizes:
    rand_vals = random.sample(range(n * 10), n)
    test_cases = {
        "Random": rand_vals,
        "Already Sorted": sorted(rand_vals),
        "Reverse Sorted": sorted(rand_vals, reverse=True),
    }

    for algo_name, algo in algorithms.items():
        for in_name, data in test_cases.items():
            t1 = time.perf_counter()
            out = algo(data)
            t2 = time.perf_counter()
            assert out == sorted(data)
            results.append({
                "Algorithm": algo_name,
                "Input Type": in_name,
                "Input Size": n,
                "Time (seconds)": t2 - t1,
            })

csv_file = "sorting_timings.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Algorithm", "Input Type", "Input Size", "Time (seconds)"]
    )
    writer.writeheader()
    writer.writerows(results)

plt.figure(figsize=(10, 6))
for algo_name in algorithms:
    rows = []
    for r in results:
        if r["Algorithm"] == algo_name and r["Input Type"] == "Random":
            rows.append(r)
    rows.sort(key=lambda x: x["Input Size"])
    x = [r["Input Size"] for r in rows]
    y = [r["Time (seconds)"] for r in rows]
    plt.plot(x, y, marker="o", label=algo_name)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Comparison - Random Input")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("random_input_comparison.png", dpi=300)
plt.close()

plt.figure(figsize=(10, 6))
for algo_name in algorithms:
    rows = []
    for r in results:
        if r["Algorithm"] == algo_name and r["Input Type"] == "Already Sorted":
            rows.append(r)
    rows.sort(key=lambda x: x["Input Size"])
    x = [r["Input Size"] for r in rows]
    y = [r["Time (seconds)"] for r in rows]
    plt.plot(x, y, marker="o", label=algo_name)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Comparison - Already Sorted Input")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("sorted_input_comparison.png", dpi=300)
plt.close()

print("Files created:")
print("1. random_input_comparison.png")
print("2. sorted_input_comparison.png")
print("3. sorting_timings.csv")

