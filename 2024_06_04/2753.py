# 연도가 주워졌을 때 윤년이면 1 아니면 0

# 윤년의 조건:
# 4의 배수 이면서 100의 배수가 아닐때 또는 400의 배수일 때

Year = int(input())

if Year%4 == 0 and Year%100 != 0 or Year%400 == 0:
    print("1")
else:
    print("0")