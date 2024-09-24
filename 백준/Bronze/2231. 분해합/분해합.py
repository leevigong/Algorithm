def sum_digit(number):
    total = 0
    for i in str(number):
        total += int(i)
    return total
    
n = int(input())

digit = len(str(n)) # 자리수 구하는 식

start = n - digit * 9
if start < 0:  # start가 0보다 작아지면 0으로 설정
    start = 0
end = n

generators = []
for m in range(start, end): # start 포함, end 미포함
   if (m + sum_digit(m) == n):        
        generators.append(m)

if generators:
    print(min(generators))
else:
    print(0)