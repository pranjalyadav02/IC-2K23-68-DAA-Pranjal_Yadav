# Task 2: Sorting Performance Comparison

The program compares Bubble, Selection, Insertion, Merge, Quick and Heap Sort with random, sorted and reverse-sorted inputs of different sizes.

It checks each result against Python's sorted output, records timings in a CSV file and saves comparison graphs.

## Complexity
The benchmark runs six algorithms over several input sizes and input orders. Its total running time depends on the chosen sizes and the algorithms; an individual run of the slowest methods is O(n²). The CSV and graph files use space proportional to the number of measurements.

## Run
Install Matplotlib first with `python -m pip install matplotlib`, then run:

`python graph.py`

The program creates `sorting_timings.csv`, `random_input_comparison.png` and `sorted_input_comparison.png`.
