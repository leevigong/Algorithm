n = int(input())
fi = [1] * n

if n >= 2:
    fi[1] = 3   
    for i in range(2, n):
        fi[i] = fi[i-1] + fi[i-2]*2

print(fi[n-1]%10007)