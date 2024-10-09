N = int(input())
fi = [1] * N

for i in range(2, N):
    fi[i] = fi[i-1] + fi[i-2]

print(fi[N-1])