# 3Sum

Given an integer list, find all unique triplets whose sum is zero.

## Approach
Sort the list. Fix one number, then use two pointers to find the other two numbers. Skip repeated values so the result does not contain duplicate triplets.

## Complexity
- Time: O(n²)
- Extra space: O(1) auxiliary space, excluding the sorting implementation and returned triplets

## Run
This file follows the LeetCode class format. The method is `Solution().threeSum(nums)`.
