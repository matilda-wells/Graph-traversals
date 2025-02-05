graph = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,0,1],
    [0,1,0,0,0,0],
    [0,1,0,0,0,1],
    [0,0,1,0,1,0]
]
# Keeps track of visited nodes
visited = [False] * len(graph)
def dfs(start):
    # Mark the current node as visited
    visited[start] = True
    print("Visited", start)
    # Go through all nodes
    for next in range(len(graph[start])):
        if graph[start][next] == 1 and not visited[next]:  # Check if connected and not visited
            dfs(next)  # Recursive call
# Start DFS from node 0
dfs(0)