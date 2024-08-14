m, n = map(int, input().split())
sieve = [True] * (n+1)
sieve[0] = sieve[1] = False

for i in range(2, n+1):
    if sieve[i]:
        for j in range(i*i, n+1, i):
            sieve[j] = False

for i in range(m, n+1):
    if sieve[i]:
        print(i)