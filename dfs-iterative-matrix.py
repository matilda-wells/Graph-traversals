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
    visited[stack] = True

dfs(graph, 0)

Empty = False

while not Empty:
    pass
