Part 1: Trace It Yourself
Given list: [8, 3, 15, 6, 2]

1. Find the largest number by checking one number at a time:
- Initial max = 8
- Compare with 3: 3 < 8, max remains 8 (comparison 1)
- Compare with 15: 15 > 8, max becomes 15 (comparison 2)
- Compare with 6: 6 < 15, max remains 15 (comparison 3)
- Compare with 2: 2 < 15, max remains 15 (comparison 4)
Total comparisons made = 4
Maximum value found = 15

2. Sort this list from smallest to largest using Merge Sort:
- Initial array: [8, 3, 15, 6, 2]
- Split into left [8, 3] and right [15, 6, 2]
- Split [8, 3] into [8] and [3] -> merge to [3, 8]
- Split [15, 6, 2] into [15] and [6, 2] -> [6, 2] splits to [6] and [2] -> merges to [2, 6]
- Merge [15] and [2, 6] -> [2, 6, 15]
- Merge [3, 8] and [2, 6, 15] -> [2, 3, 6, 8, 15]
Sorted array: [2, 3, 6, 8, 15]

