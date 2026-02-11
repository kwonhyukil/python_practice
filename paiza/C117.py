# A : 건설비용 1000
# B : 인건비 1000 / 1개월
# C : 라면 이익 50
# R : 라면 판매 수

# N : 점포 수
# M : 영업기간 3개월



# 라면이익 * 라면 판매수 - 건설비 - (인건비 * 3개월)

# 점포 수 / 월수

N, M = map(int, input().split())

# 건설비용 / 인건비 / 이익
A, B, C = map(int, input().split())

salesList = []

# 점수 당 이익 계산
for i in range(N):
  # 판매 라면수 계산
  num = int(input())
  total = (num * C) - A - (B * M)
  salesList.append(total)


count = 0

for w in salesList:
  if w < 0:
    count += 1
    
print(count)