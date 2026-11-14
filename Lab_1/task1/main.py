# Find the largest number and sort the list using merge sort

def find_max(numbers):
    if not numbers:
        return None

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    numbers = [8, 3, 15, 6, 2]
    print("Original list:", numbers)
    print("Largest number:", find_max(numbers))
    print("Sorted list:", merge_sort(numbers))
