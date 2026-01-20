N, C = map(int, input().split())
arr = list(map(int, input().split()))

major = N // 2 + 1
need = [max(0, C - a) for a in arr]
need.sort()

print(need[major - 1])
