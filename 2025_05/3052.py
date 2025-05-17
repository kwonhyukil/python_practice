namege = []


# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 인지.

for i in range(1, 11):
    # 숫자 입력 10번
    inputs = int(input())
    
    # 42로 나누었을 때 나머지
    num = inputs % 42
    if num not in namege:
        namege.append(num)

print(len(namege))