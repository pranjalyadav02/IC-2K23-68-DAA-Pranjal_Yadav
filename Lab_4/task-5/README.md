# Trapping Rain Water

Given bar heights, calculate how much rain water can be trapped between them.

## Approach
Use two pointers from both ends and keep track of the maximum height seen on each side. Add the water that can be held at the shorter side.

## Complexity
- Time: O(n)
- Extra space: O(1)

## Run
This file follows the LeetCode class format. The method is `Solution().trap(height)`.
