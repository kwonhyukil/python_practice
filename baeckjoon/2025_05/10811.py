# 입력
n, m = map(int, input().split())
baskets = list(range(1, n + 1))  # 바구니 초기화: [1, 2, 3, ..., n]

for _ in range(m):
    i, j = map(int, input().split())
    start = i - 1  # 0-based index로 보정
    end = j - 1

    # 교환 횟수는 (end - start + 1) // 2 번
    for k in range((end - start + 1) // 2):
        baskets[start + k], baskets[end - k] = baskets[end - k], baskets[start + k]

# 출력
print(*baskets)
