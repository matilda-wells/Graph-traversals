graph = [
	[0,1,1,0,0,0],
	[1,0,0,1,1,0],
	[1,0,0,0,0,1],
	[0,1,0,0,0,0],
	[0,1,0,0,0,1],
	[0,0,1,0,1,0]
]


def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    visited[start] = True

    while len(stack) > 0:
        for i in range(len(visited)):
            if  graph[start][i] == 1 and visited[i] == False:
                dfs(graph, i)

dfs(graph, 0)

