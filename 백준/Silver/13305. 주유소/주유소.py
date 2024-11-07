n = int(input())
distance = list(map(int, input().split()))  # 도시 사이 거리
price = list(map(int, input().split()))     # 도시 주유 리터당 가격

total_cost = 0
current_price = price[0]  

for i in range(n-1):

    dist = distance[i]
    
    total_cost += dist * current_price

    if price[i + 1] < current_price:
        current_price = price[i + 1]

print(total_cost)    