import heapq

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
           
def kruskal(n,graph):
    edges, total = kruskal_mst(n, graph)
    for u, v, w in edges:
      print(f'{u} - {v} (weight {w})')
    print(f'total weight: {total}\n')