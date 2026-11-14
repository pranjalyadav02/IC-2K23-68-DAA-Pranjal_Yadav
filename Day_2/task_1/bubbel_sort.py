def bubble_sort(arr):
    a = list(arr)
    n = len(a)
    i = 0
    while i < n:
        swapped = False
        j = 0
        while j < n - i - 1:
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swapped = True
            j += 1
        print("Pass", i + 1, ":", a)
        if not swapped:
            break
        i += 1
    return a


arr = [55, 34, 12, 89, 45, 23, 7]
print("Original Array:", arr)
res = bubble_sort(arr)
print("Sorted Array:", res)

