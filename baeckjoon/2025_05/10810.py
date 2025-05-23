# 입력 받기
N, M = map(int, input().split())

# 바구니 배열 초기화 (0으로 채움)
baskets = [0] * N

# 공 넣기 작업
for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i - 1, j):  # 인덱스가 0부터 시작하므로 i-1부터 j까지
        baskets[index] = k

# 출력 (공백으로 구분하여 출력)
print(" ".join(map(str, baskets)))
