# Adding Spaces to a String

Insert spaces before the character positions listed in the input array.

## Approach
Walk through the original string once. When the current index matches the next requested position, add a space before the character.

## Complexity
- Time: O(n + k), where n is the string length and k is the number of spaces
- Extra space: O(n + k) for the output

## Run
This file follows the LeetCode class format. The method is `Solution().addSpaces(s, spaces)`.
