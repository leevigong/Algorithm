n = int(input())
numbers = list(map(int, input().split()))

max_num = 1000
sieve = [True] * (max_num + 1)
sieve[0] = sieve[1] = False

for i in range(2, max_num + 1):
    if sieve[i]:
        for j in range(i * i, max_num + 1, i):
            sieve[j] = False

primes = [num for num in numbers if sieve[num]]
print(len(primes))