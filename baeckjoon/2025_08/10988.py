word = input()


word_list1 = []
word_list2 = []

for i in word:
  word_list1.append(i)


for j in range(len(word_list1)-1, -1, -1):
  word_list2.append(word_list1[j])


if word_list1 == word_list2:
  print(1)
else:
  print(0)  