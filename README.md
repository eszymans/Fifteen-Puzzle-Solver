# Fifteen Puzzle Solver

The `Fifteen Puzzle Solver` project implements a solution for the classic "Fifteen Puzzle" using various state-space search strategies. The program supports boards of any size (not only 4x4) and allows analyzing the performance of different algorithms.

## Project Goals

The project consists of two main parts:

1. Programming Part:
   - Implement algorithms to solve the puzzle:
     - BFS (Breadth-First Search)
     - DFS (Depth-First Search)
     - A* with heuristics:
       - Hamming distance
       - Manhattan distance
   - Generate a sequence of moves that transforms the initial puzzle state into the goal state.
   - Collect statistics about the computation process: solution length, number of visited and processed states, maximum recursion depth, execution time.

2. Research Part:
   - Analyze the efficiency of each search method on 413 initial puzzle states at distances 1–7 from the goal state.
   - Compare results using different neighbor exploration orders and A* heuristics.
   - Visualize data using charts and draw conclusions based on the results.

## Repository Structure

fifteen-puzzle-solver/
│
├─ src/ # Source code
│ ├─ BreadthFirstSearch.py # BFS implementation
│ ├─ DepthLimitedSearch.py # DFS implementation
│ ├─ Astar.py # A* implementation with heuristics
│ ├─ program.py # Main function with saving and reading file 
│ └─ saveInfoToFile.py # Helper function
│
├─ examples/ # Sample input and output files
│ ├─ 4x4_01_0001.txt
│ ├─ 4x4_01_0001_bfs_sol.txt
│ └─ ...
│
├─ results/ # Folder for generated statistics and charts
│
├─ README.md # This file
└─ requirements.txt # Required Python libraries


## File Formats

### Input File (Initial Puzzle State)
- First line: `w k` – number of rows and columns.
- Following lines: puzzle numbers (0 represents the empty space).

### Output File (Solution)
- First line: length of the solution (n), or `-1` if no solution exists.
- Second line: sequence of letters `L, R, U, D` representing moves of the empty space.

### Additional Information File
1. Solution length
2. Number of visited states
3. Number of processed states
4. Maximum recursion depth
5. Computation time in seconds (3 decimal places)

## Running the Program

Example commands:

```bash
# BFS with neighbor order RDUL
python src/bfs.py RDUL examples/4x4_01_0001.txt results/4x4_01_0001_bfs_rdul_sol.txt results/4x4_01_0001_bfs_rdul_stats.txt

# DFS with neighbor order LUDR
python src/dfs.py LUDR examples/4x4_01_0001.txt results/4x4_01_0001_dfs_ludr_sol.txt results/4x4_01_0001_dfs_ludr_stats.txt

# A* with Manhattan heuristic
python src/astar.py manh examples/4x4_01_0001.txt results/4x4_01_0001_astr_manh_sol.txt results/4x4_01_0001_astr_manh_stats.txt
