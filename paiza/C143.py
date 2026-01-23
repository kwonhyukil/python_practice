S = str(input())

prev = False

for i in S:
  if i == '-':
    if not prev:
      print('-', end='')
      prev = True
  else:
    print(i,end='')
    prev = False