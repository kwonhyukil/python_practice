# 단어 갯수
num = int(input())

w = []
# 갯수만큼 반복
for i in range(num):
  # 단어 입력
  word = input() # apple => ['a', 'p', 'p', 'l', 'e']
  # print(len(w))
  if (i == 0):
    w = word[-1]
  elif len(w) <= 1:
    if w[0] != word[0]:
      w = w, word[0]
      # print(w)
    else:
      w = word[-1]
if (len(w) == 1):
  print('Yes')
else:
  print(w[0], w[1])
      
  
  # 단어 검증
