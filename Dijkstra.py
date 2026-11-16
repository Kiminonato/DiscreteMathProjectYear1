import heapq

# 1. Input Section
def read_graph(filename):
    with open(filename, 'r') as file:
        # Read the first line: Number of vertices (N) and number of edges (M)
        n, m = map(int, file.readline().split())
        
        # Create an Adjacency List to store the graph (0 to N-1)
        graph = {i: [] for i in range(n)}
        
        # Loop to read M lines of edges
        for _ in range(m):
            u, v, w = map(int, file.readline().split())
            # Undirected graph requires adding edges in both directions
            graph[u].append((v, w))
            graph[v].append((u, w))
            
    return n, graph

# 2. Processing Section
def dijkstra(n, graph, start, end):
    # Initialize distances with infinity for all nodes except the start node (0)
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    
    # Keep track of previous nodes for path reconstruction
    previous = {i: None for i in range(n)}
    
    # Priority Queue storing tuples of (accumulated_distance, current_node)
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # If the destination is reached, stop early
        if current_node == end:
            break
            
        # If the current distance is greater than the recorded shortest distance, skip
        if current_dist > distances[current_node]:
            continue
            
        # Check all neighbors of the current_node
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            # Relaxation step: If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
                
    # Path reconstruction from end to start node
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = previous[curr]
    path.reverse() # Reverse the list to order from start to end
    
    # Case when there is no path connecting them
    if distances[end] == float('inf'):
        return None, float('inf')
        
    return path, distances[end]

# 3. Output & Main Section
if __name__ == "__main__":
    
    filename = 'files_test/1.txt'
    
    try:
        n, graph = read_graph(filename)
        
        start_node = int(input("Enter start node: "))
        end_node = int(input("Enter end node: "))
        
        path, total_weight = dijkstra(n, graph, start_node, end_node)
        
        if path and total_weight != float('inf'):
            path_str = " -> ".join(map(str, path))
            print(f"Path: {path_str}")
            print(f"Minimum total weight: {total_weight}")
        else:
            print(f"No path found from {start_node} to {end_node}")
            
    except FileNotFoundError:
        print(f"File {filename} not found. Please check the file path.")