n = int(input())

sum = 1
for i in range(n):
    sum *= i+1

result = []
for i in str(sum):
    result.append(i)


start = len(result)
count = 0
for i in range(start-1, -1, -1):
    if (int(result[i]) == 0):
        count += 1
    else:
        break
        
print(count)