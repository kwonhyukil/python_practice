N, M = list(map(int, input().split()))

List_A = []

for A in range(N):
  row_A = list(map(int, input().split()))
  List_A.append(row_A)

List_B = []

for B in range(N):
  row_B = list(map(int, input().split()))
  List_B.append(row_B)

for n in range(N):
  result = []
  for m in range(M):
    add = List_A[n][m] + List_B[n][m]
    result.append(add)
  
  print(*result)


# N, M = list(map(int, input().split()))

# List_A = []

# for n in range(N):
#   row_A = list(map(int, input().split()))
#   List_A.append(row_A)
  
# for n in range(N):
#   row_B = list(map(int, input().split()))
  
#   result = []
#   for m in range(M):
#     add = List_A[n][m] + row_B[m]
#     result.append(add)
    
#   print(*result)