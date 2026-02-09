a = [10, 20, 30]
h = [20, 30, 40, 50]

set_a = set(a)
set_h = set(h)

p = list(set_a & set_h)

x = list(set_a ^ set_h)

print(p)
print(x)

# 중첩: [20, 30]
# 중첩x: [10, 40, 50]

# for i in range(len(a)):

#   for j in range(len(h)):
#     if a[i] == h[j]:
#       p.append(a[i])
#       break
# print(p)
# 출력
# [20, 30]
# [10, 40, 50]
  















# ok = []
# no = []

# for i in range(len(a)):
  
#   for j in range(len(h)):
#     if a[i] == h[j]:
#       ok.append(a[i])

# print(ok)
