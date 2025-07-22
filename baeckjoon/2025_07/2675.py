T = int(input())


for _ in range(T):
  R = list(map(str, input()))

  for i in range(len(R[2:])):
    # print(i)
    for j in range(int(R[0])):
      print(R[i+2], end="")
  print()


