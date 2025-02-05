graph = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,0,1],
    [0,1,0,0,0,0],
    [0,1,0,0,0,1],
    [0,0,1,0,1,0]
]
def dfs(start):
    visited = [False] * len(graph)  # Track visited nodes
    stack = [start]  # Use stack for DFS
    while stack:
        current = stack.pop()  # Remove last element (LIFO order)
        if not visited[current]:  # Process if not visited
            visited[current] = True
            print("Visited", current)
            # Add unvisited neighbors to stack
            for neighbor in range(len(graph[current])):
                if graph[current][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
# Start DFS from node 0
dfs(0)

