# N, M = list(map(int, input("N, M 입력: ").split()))

# List_A = []

# for A in range(N):
#   row_A = list(map(int, input().split()))
#   List_A.append(row_A)

# result = []

# for n in range(N):
#   row_B = list(map(int, input().split()))
  
#   for m in range(M):
#     add = List_A[n][m] + row_B[m]
#     result.append(add)

# for i in range(len(result)):
#   print(result[i], end=' ')
#   if (i + 1) % M == 0:
#     print()

N, M = list(map(int, input().split()))

List_A = []

for n in range(N):
  row_A = list(map(int, input().split()))
  List_A.append(row_A)
  
for n in range(N):
  row_B = list(map(int, input().split()))
  
  result = []
  for m in range(M):
    add = List_A[n][m] + row_B[m]
    result.append(add)
    
  print(*result)