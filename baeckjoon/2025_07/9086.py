num = int(input())

word_list = []


for i in range(num):
  word = input()
  line = []
  for j in word:
    line.append(j)
  word_list.append(line)


for i in range(len(word_list)):
  print(word_list[i][0]+word_list[i][-1])

# 2)
# num = int(input())

# for _ in range(num):
#   word = input()
#   print(word[0] + word[-1])