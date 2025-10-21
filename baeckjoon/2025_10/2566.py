List_9x9 = []

num = 9

for i in range(num):
  r = list(map(int, input().split()))
  List_9x9.append(r)
  
max_num = 0
num_index_row = 0
num_index_col = 0

for i in range(num):
  for j in range(num):
    if (max_num <= List_9x9[i][j]):
      max_num = List_9x9[i][j]
      num_index_row = i + 1
      num_index_col = j + 1
      
print(max_num)
print(num_index_row, num_index_col)