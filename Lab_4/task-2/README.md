# Find the Index of the First Occurrence in a String

Return the starting index of the first occurrence of `needle` in `haystack`. Return -1 if it is not found. An empty needle returns 0.

## Approach
Check each possible starting position and compare the substring with the needle.

## Complexity
- Time: O((n - m + 1) × m) in the worst case
- Extra space: O(m) for the temporary substring comparison in Python

## Run
This file follows the LeetCode class format. The method is `Solution().strStr(haystack, needle)`.
