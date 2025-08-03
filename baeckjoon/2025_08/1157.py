word = input().upper()

alphabet_count = {}

for i in word:
  if i in alphabet_count:
    alphabet_count[i] += 1
  else:
    alphabet_count[i] = 1

max_count = max(alphabet_count.values())
most_frequent = [k for k,v in alphabet_count.items() if v == max_count]

if (len(most_frequent) > 1):
  print('?')
else:
  print(most_frequent[0])
