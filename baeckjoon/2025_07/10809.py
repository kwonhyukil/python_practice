word = list(map(str, input()))

alphabet = [chr(i) for i in range(97,123)]
# a = 1 z = 공백

for i in alphabet:
  if i in word:
    print(word.index(i), end=' ')
  else:
    print(-1, end=' ')