from comparison import Comparison
from sorting import Sorting

if __name__ == "__main__":
    nums = [8, 3, 15, 6, 2]
    print("Original list:", nums)
    c = Comparison()
    max_val = c.compare(nums)
    print("The maximum value is:", max_val)
    s = Sorting()
    sorted_nums = s.sort(nums)
    print("Sorted list:")
    for x in sorted_nums:
        print(x, end=" ")
    print()

