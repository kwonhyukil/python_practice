# 갯수, 할인기준
N, L = map(int, input().split())

arr = list(map(int, input().split()))
# print(arr)
# arr.sort()
# print(arr, arr[-1])
# print(sum(arr))
a = max(arr)

total = 0

for i in arr:
  if (i == a and L <= a):
    total += a/2
  else:
    total += i

print(int(total))