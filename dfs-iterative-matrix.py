graph = [
	[0,1,1,0,0,0],
	[1,0,0,1,1,0],
	[1,0,0,0,0,1],
	[0,1,0,0,0,0],
	[0,1,0,0,0,1],
	[0,0,1,0,1,0]
]

VISITED = 0
UNVISITED = 0

def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    # visited[start] = True

    # while len(stack) > 0:
    #     for i in range(len(visited)):
    #         if  graph[start][i] == 1 and visited[i] == False:
    #             dfs(graph, i)

    visited[start] = True
    current = start
    while len(stack) > 0:
        found = False
        # find an unvisited neighbour of the current node
        for neighbour in range(len(graph)):
            if graph[current][neighbour] == 1 and visited[neighbour] == False:
                stack.append(neighbour)
                found = True
        # no unvisited neighbours - pop from the stack
        if not found:
            current = stack.pop()


 
dfs(graph, 0)

