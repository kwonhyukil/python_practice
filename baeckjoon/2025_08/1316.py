n = int(input())
count = 0

for _ in range(n):
  word = input()
  used = []
  prev = ''
  ok = True

  for i in word:
    if i != prev:
      if i in (used):
        ok = False
        break
      used.append(i)
      prev = i

  if ok:
    count += 1

print(count)