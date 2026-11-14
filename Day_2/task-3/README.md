# Task 3: Keyword Search

A small keyword-search program that compares Binary Search with two hash-table collision methods: chaining and linear probing.

## Complexity
- Binary Search: O(log n) search time after sorting the terms; O(n log n) to prepare the sorted list.
- Hash table search: O(1) average time, O(n) worst case when many terms collide.
- Chaining uses O(n + m) space for n terms and m buckets. Linear probing uses O(m) table space.

## Run
`python search_engine.py`
