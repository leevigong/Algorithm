n = int(input())

meetings = []
num = 0
for _ in range(n):
    m = list(map(int, input().split())) 
    meetings.append(m)

meetings.sort(key=lambda x: (x[1],x[0]))
# meetings.sort(key=lambda x: x[1])

cnt = 0
end_time = 0

for meet in meetings:
    start, end = meet
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)