def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print("Checking index:", mid, "Value:", arr[mid])
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [12, 24, 32, 45, 53, 67, 78, 89]
print("Array:", arr)

key = 53
idx = binary_search(arr, key)
if idx != -1:
    print(key, "found at index", idx)
else:
    print(key, "not found")

print("--------------------")

key = 50
idx = binary_search(arr, key)
if idx != -1:
    print(key, "found at index", idx)
else:
    print(key, "not found")

