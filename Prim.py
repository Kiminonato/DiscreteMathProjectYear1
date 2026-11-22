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

def prim_mst(n, graph):
    if not graph:return [], 0

    start_node = next(iter(graph))
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

if __name__ == '__main__':
    n, graph = read_graph('YOUR FILES LOCATION')
    edges, total = prim_mst(n, graph)
    for u, v, w in edges:
      print(f'{u} - {v} (weight {w})')
    print(f'total weight: {total}\n')