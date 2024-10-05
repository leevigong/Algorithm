n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visted = [0] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

def dfs(node, depth):
  visted[node] = 1
  #
  if(node == b):
    # print(depth)
    return depth
  
  for i in graph[node]:
    if visted[i] != 1:
      result = dfs(i, depth + 1)
      if result != -1: 
          return result
  return -1
result = dfs(a, 0)
print(result if result else -1)