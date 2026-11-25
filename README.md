# Graph Algorithms Project (CSS113)

A Python CLI application implementing core undirected, weighted graph algorithms—**Dijkstra's Shortest Path**, **DFS & BFS Traversal**, **Prim's MST**, and **Kruskal's MST**—built for Discrete Mathematics (`CSS113`).

## Language & Version

- **Python 3.10+** (Required for structural pattern matching `match-case` in `main.py`)
- **Standard Library Only:** Uses built-in `collections.deque` and `heapq` with zero third-party dependencies.

## Installation

Clone the repository and make sure **Python 3.10+** is installed on your system:

```bash
git clone https://github.com/Kiminonato/DiscreteMathProjectYear1.git
cd DiscreteMathProjectYear1
```

## Input Data Format

Graph test cases are stored as .txt files inside test_case/ (e.g., 1_Example.txt, 4_cycle_graph.txt, 7_disconnected.txt, 10_zero_weight_edges.txt).
- **Line 1:** n m — number of vertices (0 to n - 1) and number of edges.
- **Next m lines:** u v w — an undirected edge connecting vertex u and vertex v with weight w.

## Example Input 
```text
5 6 
0 1 2 
0 2 5 
1 2 1 
1 3 4 
2 4 3 
3 4 2 
```

## How to Run & Example Commands

1. Open main.py and update filename (line 21) to point to your target graph file (for example, "test_case/1_Example.txt").
2. Run the program from the project root in your terminal:

```bash
python main.py
```

- Pick an option (1–4) from the menu and provide the requested vertex inputs:
- **Example**

```text
Graph algorithms
(1)Dijkstra
(2)DFS, BFS
(3)Prim
(4)Kruskal

Choose algorithm to calculate: 1
Enter start node: 0
Enter end node: 4

Path: 0 -> 1 -> 2 -> 4
Minimum total weight: 6
```

## Limitations

- **Graph Type:** Assumes an undirected graph with vertices indexed from `0` to `n - 1`; shortest-path results assume non-negative edge weights.
- **Disconnected Graphs:** Queries on disconnected graphs only cover reachable nodes or separate components (e.g., no valid path between unreachable nodes in Dijkstra, or separate spanning components in MST).
- **CLI & File Input:** Requires updating the `filename` path in `main.py` before running, and entering vertex indices manually via the terminal for algorithms that require them (not required for Kruskal's MST).
- **Integer-Only & Exact Line Count:** All values (`n`, `m`, `u`, `v`, `w`, and CLI prompts) must be integers. The file must contain `m` edge lines matching the header `n m`, and vertex indices must stay within `0` to `n - 1`.
