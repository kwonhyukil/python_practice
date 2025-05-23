# 1 에서 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는다


# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
num_1, num_2, num_3 = map(int,input().split())

# 같은 눈이 3개가 나오면 10,000원 + (같은 눈) * 1,000원의 상금을 받게 된다.
if num_1 == num_2 == num_3:

    print(10000+num_1*1000)

# 같은 눈이 2개가 나오는 경우에는 1,000 + (같은 눈) * 100원의 상금을 받게 된다.
elif num_1 == num_2:
    print(1000+num_1 *100)
elif num_2 == num_3:
    print(1000+num_2 *100)
elif num_1 == num_3:
    print(1000+num_3 *100)
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) * 100원의 상금을 받게 된다.
# elif num_1 > num_2 or num_2 > num_3:
elif num_1 > num_2 and num_1 > num_3:
    print(num_1*100)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2*100)
elif num_3 > num_1 and num_3 > num_2:
    print(num_3*100)