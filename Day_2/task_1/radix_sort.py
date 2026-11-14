def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    i = 0
    while i < n:
        idx = (arr[i] // exp) % 10
        count[idx] += 1
        i += 1

    i = 1
    while i < 10:
        count[i] += count[i - 1]
        i += 1

    i = n - 1
    while i >= 0:
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
        i -= 1

    i = 0
    while i < n:
        arr[i] = output[i]
        i += 1


def radix_sort(arr):
    a = list(arr)
    if len(a) == 0:
        return a

    for val in a:
        if val < 0:
            raise ValueError("Only non-negative numbers allowed")

    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        counting_sort(a, exp)
        print("After exp", exp, ":", a)
        exp *= 10

    return a


arr = [182, 35, 90, 704, 12, 5, 88]
print("Original Array:", arr)
result = radix_sort(arr)
print("Sorted Array:", result)

