from collections import deque

def readgraph(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())

        graph = [[] for _ in range(n)]

        for _ in range(m):
            u, v, w = map(int, file.readline().split())

            # Undirected graph
            graph[u].append((v, w))
            graph[v].append((u, w))

    return n, graph

def dfs(graph, start):
    visited = set()
    visit_order = []
    tree_edges = []

    def search(u):
        visited.add(u)
        visit_order.append(u)

        for v, w in graph[u]:
            if v not in visited:
                tree_edges.append((u, v, w))
                search(v)

    search(start)

    return visit_order, tree_edges


def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    visit_order = []
    tree_edges = []

    while queue:
        u = queue.popleft()
        visit_order.append(u)

        for v, w in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

                tree_edges.append((u, v, w))

    return visit_order, tree_edges

def print_result(name, visit_order, tree_edges):
    print(f"\n===== {name} =====")

    print("Visit Order:", " -> ".join(map(str, visit_order)))

    print("Tree Edges:")
    for u, v, w in tree_edges:
        print(f"{u} -- {v} (Weight: {w})")

    print("Total Vertices:", len(visit_order))
    print("Total Tree Edges:", len(tree_edges))


n, graph = readgraph("YOUR FILES LOCATION")

start = int(input("Enter starting vertex: "))

if start < 0 or start >= n:
    print("Invalid starting vertex")
else:
    dfs_order, dfs_edges = dfs(graph, start)
    bfs_order, bfs_edges = bfs(graph, start)

    print_result("DFS", dfs_order, dfs_edges)
    print_result("BFS", bfs_order, bfs_edges)