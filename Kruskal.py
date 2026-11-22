import heapq
def read_graph(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        graph = {}

        for _ in range(m):
            parts = file.readline().split()
            u, v, w = parts[0], parts[1], int(parts[2])
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))
    return len(graph), graph

def kruskal_mst(n, graph):
    if not graph:
        return [], 0
    
    min_heap = []
    for u in graph:
        for v, w in graph[u]:
             if u < v:
                 min_heap.append((w, u, v))
    heapq.heapify(min_heap)

    parent = {node: node for node in graph}

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1
            return True
        return False

    mst_edges = []
    total_weight = 0

    while min_heap and len(mst_edges) < n - 1:
        weight, u, v = heapq.heappop(min_heap)
        if union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
    return mst_edges, total_weight
           


if __name__ == '__main__':
    n, graph = read_graph('YOUR FILES LOCATION')
    edges, total = kruskal_mst(n, graph)
    for u, v, w in edges:
      print(f'{u} - {v} (weight {w})')
    print(f'total weight: {total}\n')