N = int(input())

win_count = 0

for i in range(N):
  L, B = map(str, input().split())
  if (L == 'G' and B == 'C'):
    win_count += 1
  if (L == 'C' and B == 'P'):
    win_count += 1
  if (L == 'P' and B == 'G'):
    win_count += 1

print(win_count)
    