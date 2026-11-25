from DFS_BFS import dfs_bfs
from Dijkstra import dijkstra
from Prim import prim
from Kruskal import kruskal

def read_graph(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())

        graph = {i: [] for i in range(n)}
        
        for _ in range(m):
            u, v, w = map(int, file.readline().split())

            graph[u].append((v, w))
            graph[v].append((u, w))
            
    return n, graph

if __name__ == "__main__":
    filename = "ProjectCSS113/test_case/1_Example.txt"
    try:
        n, graph = read_graph(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file path.")
        raise SystemExit(1)
    except (ValueError, KeyError) as e:
        print(f"Error reading graph file: {e}")
        raise SystemExit(1)

    print("Graph algorithms")
    print("(1)Dijkstra\n(2)DFS, BFS\n(3)Prim\n(4)Kruskal\n")
    
    try:
        user_choose = int(input("Choose algorithm to calculate: "))
    except ValueError:
        print("Please enter a number (1-4).")
        raise SystemExit(1)
    
    match user_choose:
        case 1:
            dijkstra(n, graph)
        case 2:
            dfs_bfs(n, graph)
        case 3:
            prim(n, graph)
        case 4:
            kruskal(n, graph)
        case _:
            print("Invalid choice. Please choose a number between 1 and 4.")