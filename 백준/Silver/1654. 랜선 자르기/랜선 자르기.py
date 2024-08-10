k, n = map(int,input().split())
k_list = []
for _ in range(k):
    k_list.append(int(input()))

start = 1
end = max(k_list)

while start <= end:
    sum = 0

    mid = (start + end) // 2
    for j in k_list:
        sum += j//mid

    if sum >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)