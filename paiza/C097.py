# 선물 A : X의 배수
# 선물 B : Y의 배수
# 선물 AB : X의 배수 이면서 Y의 배수 일때 

# 응모자 N

# N X Y
N, X, Y = map(int, input().split())

# N 응모자 수 ( 1 ~ N )


for i in range(1, N+1):
    
    if i % X == 0 and i % Y == 0:
        print("AB")
    elif i % Y == 0:
        print("B")
    elif i % X == 0: 
        print("A")
    else:
        print("N")