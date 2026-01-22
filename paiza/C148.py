N, level = map(int, input().split())

for i in range(N):
  Y = int(input())
  if (level > Y):
    level += int(Y / 2)
  elif (level < Y):
    level = int(level / 2)

print(level)

# 횟수, 레벨
A, B = map(int, input().split())

my_level = B

for i in range(A):
  print(i)