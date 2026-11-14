# Task 4: Matrix Calculator

The program performs matrix addition, multiplication, transpose and determinant calculation for 2×2 and 3×3 matrices.

## Complexity
For matrices of compatible dimensions:
- Addition: O(r × c) time
- Multiplication (r×c by c×p): O(r × c × p) time
- Transpose: O(r × c) time
- 2×2 or 3×3 determinant: O(1) time
- Extra space for the result: O(r × c) for addition/transpose and O(r × p) for multiplication

## Run
`python matrix_cal.py`
