from collections import deque

N, M, V = map(int, input().split())  

# 인접 행렬
graph = list([0]*(N+1) for _ in range(N+1)) 
for _ in range(M):
    s, d = map(int, input().split())
    graph[s][d] = graph[d][s] = 1

# 방문 기록 행렬
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

# dfs
def dfs(node):
    visited1[node] = 1 # 방문
    print(node, end=' ')
    for i in range(1, N+1):
        if graph[node][i] == 1 and visited1[i] == 0:
            dfs(i)
# bfs
def bfs(node):
    queue = deque([node])
    visited2[node] = 1 
    while queue:
        node = queue.popleft()
        print(node, end=' ')    
        for i in range(1, N+1):
            if(graph[node][i] == 1 and visited2[i] == 0):
                queue.append(i)
                visited2[i] = 1
## 
dfs(V)
print()
bfs(V)