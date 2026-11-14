def selection_sort(arr):
    a = list(arr)
    n = len(a)
    i = 0
    while i < n - 1:
        min_idx = i
        j = i + 1
        while j < n:
            if a[j] < a[min_idx]:
                min_idx = j
            j += 1
        if min_idx != i:
            temp = a[i]
            a[i] = a[min_idx]
            a[min_idx] = temp
        print("Pass", i + 1, ":", a)
        i += 1
    return a


arr = [29, 10, 14, 37, 13]
print("Original Array:", arr)
res = selection_sort(arr)
print("Sorted Array:", res)

