import random

# 사용자로부터 난수 생성 갯수와 범위

# 사용자로 부터 3개를 입력받는다

# 생성할 난수의 수
un = 10
us = 1
ue = 5
# user_num = int(input("난수의 개수를 입력하세요: "))
# # 난수의 발생 시작 값
# user_start = int(input("시작 범위를 입력하세요: "))
# # 난수의 발생 끝 값
# user_end = int(input("끝 범위를 입력하세요: "))

a = random.randrange(1, 10)

# 저장된 랜덤 숫자 리스트
save_list = []

# 추가된 난수 카운트 리스트
count = 0
count_list = []

# 생성된 난수
adsf = []

# 사용자가 입력한 난수의 수 만큼 반복 -> for 문사용

for _ in range(un):
# 발생된 난수를 리스트에 추가
    creat_num = random.randrange(us, ue+1)
    print(creat_num , end=" ")
    adsf.append(creat_num)
    if len(save_list) == 0:
        save_list.append(creat_num)
        count_list.append(count)
        continue
# save 리스트를 순회하며 중복되는 숫자가 없을 경우 추가
    for i in range(len(save_list)):
        if creat_num not in save_list:
            save_list.append(creat_num)
            count_list.append(count)
        break

for i in range(len(save_list)):
    
    for j in range(len(adsf)):
        if save_list[i] == adsf[j]:
            count_list[i] += 1

print()
print(adsf)
print(save_list)
print(count_list)


Top = []

print("가장 많이 등장한 숫자 Top 3 (동점 포함)")
for rank in count_list:
    for i in range(len(count_list)):
        if rank > Top[i]:
            Top.insert(i, rank)
            break
    else:
        Top.append(rank)

for i in range(len(Top)):
    print(f"{save_list[i]} -> {count_list[i]}회")


# 난수를 리스트에 추가하면서 count 리스트에도 반영

# 카운트 리스트를 순회하며 저장 리스트와 일치하는 인덱스 번호와 같이 불러오기

# 동점시 전부 출력



# 자주 발생한 숫자 3개를 출력

