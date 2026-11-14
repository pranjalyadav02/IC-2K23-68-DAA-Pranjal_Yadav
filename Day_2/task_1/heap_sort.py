def heap_sort(arr):
    a = list(arr)
    n = len(a)

    def heapify(size, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and a[left] > a[largest]:
            largest = left

        if right < size and a[right] > a[largest]:
            largest = right

        if largest != i:
            temp = a[i]
            a[i] = a[largest]
            a[largest] = temp
            heapify(size, largest)

    i = n // 2 - 1
    while i >= 0:
        heapify(n, i)
        i -= 1

    print("Max Heap:", a)

    i = n - 1
    while i > 0:
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        heapify(i, 0)
        print("Pass:", a)
        i -= 1

    return a


arr = [18, 5, 21, 9, 14, 2]
print("Original Array:", arr)
result = heap_sort(arr)
print("Sorted Array:", result)

