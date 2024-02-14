## Eight Puzzle Solver with Breadth-First Search

### Description
- Eight Puzzle is a square puzzle dividing into eight sub-squares which are shuffled. The ninth square is let-free for the movement of each piece. The idea is to move sub-squares piece by piece to obtain the original content back.
- This project aims to solve Eight Puzzle by using brute-force Breadth-First Search technique.
- The outcome of this project is for self-learning to understand how graph-traversal algorithms could be implemented in the context of gaming.

### Dependencies
- Numpy

### Instructions

```
# Enter project directory
cd <project_directory>

# Create a directory for test_case
mkdir test_case

# Run main script
python3 main.py

# Run plot script to plot the outcome
python3 utils/plot.py
```

### Demo Output
- Initial State: |[4, 7, 8], [2, 1, 5], [3, 6, 0]|
- Goal State: |[1, 4, 7], [2, 5, 8], [3, 6, 0]|

```
4 7 8 2 1 5 3 6 0
4 7 8 2 1 5 3 0 6
4 7 8 2 1 5 0 3 6
4 7 8 0 1 5 2 3 6
4 7 8 1 0 5 2 3 6
4 7 8 1 5 0 2 3 6
4 7 0 1 5 8 2 3 6
4 0 7 1 5 8 2 3 6
0 4 7 1 5 8 2 3 6
1 4 7 0 5 8 2 3 6
1 4 7 2 5 8 0 3 6
1 4 7 2 5 8 3 0 6
1 4 7 2 5 8 3 6 0
```

