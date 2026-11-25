# DSA — Data Structures and Algorithms

A Python practice repository for learning Data Structures and Algorithms through small, readable programs.

## Complexity reference

| Program / operation | Time complexity | Auxiliary space | Notes |
|---|---:|---:|---|
| `1.py` average / high-low / zero count | O(n) | O(1) | Each scans the list once (average uses a sum). |
| `1.py` mode | O(n) expected | O(k) | Counter stores frequencies for k distinct values; ties keep the first value in input order. |
| `2.py` undo / redo | O(1) per operation | O(h) total | h is the number of saved history states. |
| `3.py` linear search | O(n) | O(1) | May inspect every element. |
| `3.py` binary search | O(log n) | O(1) | Input must be sorted ascending. |
| `4.py` selection sort | O(n²) | O(n) | Returns a copy; not stable. |
| `4.py` bubble sort | O(n²) worst; O(n) best | O(n) | Returns a copy and stops early if already sorted. |
| `5.py` hash-table insert/search/delete | O(1) average; O(n) worst | O(n) table storage | Separate chaining; collisions can form a long bucket. |
| `dsl1.py` BST search/insert/delete | O(log n) average; O(n) worst | O(h) recursion | h is tree height; sorted insertion can make the tree skewed. |

Complexities describe the algorithms in the current example implementations; they are not guarantees for every input.

## Current contents

The repository currently contains standalone Python exercise files:

- `1.py` — list-based library borrowing statistics (average, high/low, zero count, mode)
- `2.py` — stack-based undo and redo demonstration
- `3.py` — linear search and binary search
- `4.py`, `5.py`, and `dsl1.py` — additional practice programs; inspect each file for its exact exercise before running

## Requirements

- Python 3.10 or newer
- No third-party packages are required by the currently documented exercises

Check your Python installation:

```bash
python --version
```

## Run a program

From the repository root:

```bash
python 1.py
python 2.py
python 3.py
```

Replace the filename with the exercise you want to practise. On systems where the Python 3 command is `python3`, use `python3 1.py`.

## How to practise

For every new problem, document:
1. Problem statement and sample input/output
2. Approach and algorithm
3. Function-by-function explanation
4. Time and auxiliary-space complexity
5. Edge cases and manual tests

For binary search, ensure the input is sorted before calling the function.

## Learning roadmap

Arrays and strings → searching and sorting → stacks and queues → linked lists → hashing → recursion → trees and BSTs → graphs → greedy algorithms → dynamic programming.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep solutions beginner-friendly, function-based where appropriate, and add a short explanation with each exercise.
