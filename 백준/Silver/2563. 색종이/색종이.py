paper = [[0 for _ in range(101)] for _ in range(101)] # 도화지 : 100*100 2차원 배열(모든부분을 0으로 색칠) 
n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))

    for row in range(x, x+10):
        for col in range(y, y+10):
            paper[row][col] = 1     # 색종이: 해당 부분 1로 색칠하기

# 색칠된 1부분 구하기
result = 0
for r in paper:
    result += r.count(1)
print(result)