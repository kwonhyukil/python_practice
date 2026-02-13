# N 명으로 구성된 수업
# 투표 => 가장 많이 받은사람 대표, 중복은 없음

N = int(input().strip())

selectList = []
selectNum = []

for _ in range(N):
    x = input().strip()

    if x not in selectList:
        selectList.append(x)
        selectNum.append(1)
    else:
        idx = selectList.index(x)
        selectNum[idx] += 1

# 최다 득표자 찾기
max_idx = 0
for i in range(1, len(selectNum)):
    if selectNum[i] > selectNum[max_idx]:
        max_idx = i

print(selectList[max_idx])
