n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort() # n_list 오름차순 정렬

count = {}
for i in n_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in m_list:
    if i in count:
        print(count[i], end=' ')
    else:
        print('0', end=' ')