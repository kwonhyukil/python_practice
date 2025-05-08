N, M = map(int, input().split())

baskets = [i for i in range(1,N+1)]
temp = 0

print(baskets)

for _ in range(M):
    i, j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp

for i in range(len(baskets)):
    print(baskets[i], end=' ')


