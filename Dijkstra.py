import heapq

def dijkstra_algoritm(n, graph, start, end):
    if start not in range(n) or end not in range(n):
        return None, float('inf')

    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0

    previous = {i: None for i in range(n)}
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == end:
            break
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = previous[curr]
    path.reverse()
    
    if distances[end] == float('inf'):
        return None, float('inf')
    return path, distances[end]

def dijkstra(n,graph):
    start_node = int(input("Enter start node: "))
    end_node = int(input("Enter end node: "))
        
    path, total_weight = dijkstra_algoritm(n, graph, start_node, end_node)
        
    if path and total_weight != float('inf'):
        path_str = " -> ".join(map(str, path))
        print(f"\nPath: {path_str}")
        print(f"Minimum total weight: {total_weight}")
    else:
        print(f"No path found from {start_node} to {end_node}")