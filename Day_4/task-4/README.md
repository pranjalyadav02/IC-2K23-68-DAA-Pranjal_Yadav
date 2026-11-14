# Boats to Save People

Find the minimum number of boats needed when each boat can carry at most two people and has a fixed weight limit.

## Approach
Sort the weights. Pair the lightest person with the heaviest when they fit; otherwise, send the heaviest person alone.

## Complexity
- Time: O(n log n), mainly for sorting
- Extra space: O(1) auxiliary space, excluding sorting implementation details

## Run
This file follows the LeetCode class format. The method is `Solution().numRescueBoats(people, limit)`.
