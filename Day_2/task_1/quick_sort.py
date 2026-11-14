def quick_sort(arr):
    a = list(arr)

    def partition(low, high):
        pivot = a[high]
        i = low - 1
        j = low
        while j < high:
            if a[j] <= pivot:
                i += 1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            j += 1
        temp = a[i + 1]
        a[i + 1] = a[high]
        a[high] = temp
        print("After partition:", a)
        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(a) - 1)
    return a


arr = [24, 9, 31, 14, 5, 18]
print("Original Array:", arr)
result = quick_sort(arr)
print("Sorted Array:", result)

