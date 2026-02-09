# 조건 -1 은 뭐든 다 OK

# 쿠폰 [1, 2, 3]
# 카트 [1, 2, 3, 4] OK
# 카트 [1, -1, 3]   OK
# 카트 [2, 3, 4, 5] X

# Cu = [1, 2, 3]
# Cart =  [1, 2, 3, 4]


# Cu = [1, 2, 3]
# Cart =  [1, -1, 3]

Cu = [1, 2, 3]
Cart =  [2, 3, 4, 5]

count = 0
index = 0
if (len(Cu) <= len(Cart)):
  print("Success")
  for i in Cart:
    if index < len(Cu) and i == Cu[index]:
      index += 1
    elif i == -1:
      index += 1

if index == len(Cu):
  print("쿠폰 적용")
else:
  print("쿠폰 미적용")