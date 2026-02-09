S = input()
N = int(input())

wordList = []

for i in range(N):
  word = input()
  wordList.append(word)

for j in wordList:
  if S in j:
    print("Yes")
  else:
    print("No")