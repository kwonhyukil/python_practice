# word_list = []

# for _ in range(5):
#   w_i = list(input())
#   md_l = []
#   for i in w_i:
#     md_l.append(i)
#   word_list.append(w_i)
  
# for i in range(len(word_list)):
#   word_len = len(word_list[i])
#   print("i: ", i)
#   print("word_len: ", word_len)
#   # print(word_list[i])
#   for j in range(5):
#     if (j >= word_len):
#       continue
#     # print(j)
#     print(word_list[j][i],end='')
#     print()

word_list = []

for _ in range(5):
  word_list.append(list(input().strip()))
  
max_len = max(len(w) for w in word_list)

for i in range(max_len):
  
  for j in range(5):
    
    if i < (len(word_list[j])):
      print(word_list[j][i],end='')