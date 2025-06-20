def calculate(*arg, **kwargs):
    # 반환 딕셔너리
    D_L = {}
    # 받은 인자값 k에 저장하여 사용
    if len(arg) == 0:
        return None
    if len(kwargs) == 0:
        return None

    # 합계
    add = 0
    for i in arg:
        add += i
    # 평균
    avg = add / len(arg)
    # 최댓값
    max_num = 0
    for i in arg:
        if max_num < i:
            max_num = i
    # 최소값
    min_num = 0
    for i in range(len(arg)):
        if i == 0:
            min_num = arg[0]
        if min_num > arg[i]:
            min_num = arg[i]

    for i in kwargs:
        if i == "avg":
            D_L["avg"] = avg
            # print("avg")
        elif i == "sum":
            D_L["sum"] = add
            # print("sum")
        elif i == "max":
            D_L["max"] = max_num
            # print("max")
        elif i == "min":
            D_L["min"] = min_num
            # print("min")
        else:
            return None
            # print("None")


    return D_L



# 출력 : 함수 호출, 인자 값 전달
print(calculate(10, 20, 30, avg=True))
print(calculate(1, 2, 3, sum=True, max=True))
print(calculate(100, 50, 200, min=True, max=True, avg=True))
print(calculate(avg=True))
print(calculate(1, 2, 3))
print(calculate(1, 2, 3, total=True))