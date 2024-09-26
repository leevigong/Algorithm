from collections import deque

n = int(input())
num = []
for i in range(n):
    num.append(i+1)

num = deque(num)

while(len(num) > 1):
    num.popleft()   
    num.rotate(-1)

print(num[0])