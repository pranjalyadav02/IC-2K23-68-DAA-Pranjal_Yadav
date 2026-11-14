# Task 3: Sparse Matrix

A sparse matrix contains mostly zero values. This program stores only non-zero values as row, column and value entries. It can rebuild the original matrix and add two sparse matrices.

## Complexity
For an r by c matrix with k non-zero values:
- Convert to sparse form: O(r × c) time and O(k) extra space
- Reconstruct: O(r × c + k) time and O(r × c) space
- Add two sorted sparse representations: O(k1 + k2) time and O(k1 + k2) extra space

## Run
`python parse_matrix.py`
