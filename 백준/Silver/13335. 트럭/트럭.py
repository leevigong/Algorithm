from collections import deque

n, w, L = map(int, input().split())

trucks = list(map(int, input().split()))

queue = deque([0] * w) # 다리의 칸이라고 생각
total_weight = 0  # 현재 다리 위 트럭들의 총 무게
index = 0         # 트럭 인덱스
time = 0 
    
while index < n or total_weight > 0:
    time += 1
    
    total_weight -= queue.popleft()
    
    if index < n and total_weight + trucks[index] <= L:
        # 다리에 트럭이 올라감
        queue.append(trucks[index])
        total_weight += trucks[index]
        index += 1
    else:
        queue.append(0)
        
print(time)