def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    i = 1
    while i < n:
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print("Pass", i, ":", a)
        i += 1
    return a


arr = [15, 9, 24, 6, 31, 18]
print("Original Array:", arr)
res = insertion_sort(arr)
print("Sorted Array:", res)

