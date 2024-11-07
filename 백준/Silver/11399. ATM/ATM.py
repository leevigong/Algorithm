n = int(input())

time = list(map(int, input().split()))

time.sort()

result = []
seq = 0
for i in time:
    seq += i
    result.append(seq)

print(sum(result))