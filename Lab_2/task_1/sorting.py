# Basic sorting algorithms and binary search

def bubble_sort(a):
    a = a.copy()
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(a):
    a = a.copy()
    for i in range(len(a) - 1):
        smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return a


def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a


def merge_sort(a):
    if len(a) <= 1:
        return a.copy()
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def quick_sort(a):
    if len(a) <= 1:
        return a.copy()
    pivot = a[-1]
    smaller = [x for x in a[:-1] if x <= pivot]
    larger = [x for x in a[:-1] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)


def heap_sort(a):
    a = a.copy()
    n = len(a)

    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size and a[left] > a[largest]:
            largest = left
        if right < size and a[right] > a[largest]:
            largest = right
        if largest != root:
            a[root], a[largest] = a[largest], a[root]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(end, 0)
    return a


def radix_sort(a):
    a = a.copy()
    if not a:
        return a
    if any(value < 0 for value in a):
        raise ValueError("Radix sort here supports non-negative integers only")

    place = 1
    largest = max(a)
    while largest // place > 0:
        count = [0] * 10
        output = [0] * len(a)
        for value in a:
            digit = (value // place) % 10
            count[digit] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for value in reversed(a):
            digit = (value // place) % 10
            output[count[digit] - 1] = value
            count[digit] -= 1
        a = output
        place *= 10
    return a


def binary_search(a, target):
    low, high = 0, len(a) - 1
    while low <= high:
        middle = (low + high) // 2
        if a[middle] == target:
            return middle
        if a[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


if __name__ == "__main__":
    numbers = [29, 10, 14, 37, 13]
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Radix Sort", radix_sort),
    ]

    print("Original list:", numbers)
    for name, algorithm in algorithms:
        print(name + ":", algorithm(numbers))

    sorted_numbers = merge_sort(numbers)
    target = 14
    print("Sorted list for binary search:", sorted_numbers)
    print("Index of", target, ":", binary_search(sorted_numbers, target))
