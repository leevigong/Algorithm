from collections import deque 
import sys

n = int(input())
queue = deque()

while(n > 0):
    n -= 1
    cmd = sys.stdin.readline().rstrip()

    if cmd.startswith("push"):
        num = cmd.split()[1]
        queue.append(num)

    elif cmd.startswith("pop"):
        if(len(queue) == 0):
            print(-1)
            continue
        else:
            print(queue[0])
        queue.popleft()

    elif cmd.startswith("size"):
        print(len(queue))

    elif cmd.startswith("empty"):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)

    elif cmd.startswith("front"):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])

    elif cmd.startswith("back"):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])