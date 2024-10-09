N = int(input())

a = [0] * (N + 1) # 끝자리가 0
b = [0] * (N + 1) # 끝자리가 1

if N >= 1:
    b[1] = 1  # n=0일떄 '1'
if N >= 2:
    a[2] = 1  # n=1일때 '10'

for i in range(2, N + 1):
    a[i] = a[i - 1] + b[i - 1]  # 끝자리가 0인 경우
    b[i] = a[i - 1]             # 끝자리가 1인 경우


print(a[N]+b[N])