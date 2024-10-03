from collections import deque

def dfs(node, visited):
    visited.append(node)
    print(node, end=' ')
    indexes = [i for i, x in enumerate(graph[node]) if x == 1]
    for i in indexes:
        if i not in visited:
            dfs(i, visited)
    
def bfs(start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            indexes = [i for i, x in enumerate(graph[node]) if x == 1]
            queue.extend(indexes)
    print(*visited)    

N, M, V = map(int, input().split())  
graph = list([0]*(N+1) for _ in range(N+1)) 


for _ in range(M):
    s, d = map(int, input().split())
    graph[s][d] = graph[d][s] = 1


visited = []
dfs(V, visited)
print()

bfs(V)