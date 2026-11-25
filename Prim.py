import heapq

def prim_mst(n, graph, start_node):
    if not graph:return [], 0

    visited = set()
    min_heap = [(0, None, start_node)]
    mst_edges = []
    total_weight = 0

    while min_heap and len(visited) < n:
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
          continue

        visited.add(v)
        if u is not None:
            mst_edges.append((u, v, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return mst_edges, total_weight

def prim(n,graph):
    start = int(input("Enter starting vertex: "))
    edges, total = prim_mst(n, graph, start)
    if not edges and total == 0:
        print("Start vertex not found or graph is empty.")
        return 0
    for u, v, w in edges:
      print(f'{u} - {v} (weight {w})')
    print(f'total weight: {total}\n')