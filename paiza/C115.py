# 입력
N, M = map(int, input().split())
A = [int(input()) for _ in range(N - 1)]

# 정체 구간만 합산
result = sum(a for a in A if a <= M)

# 출력
print(result)
