# 1번자리 자연수
number_1 = int(input())
# 2번자리 자연수
number_2 = int(input())
# 3번자리 472 * 5
number_3 = (number_1*(number_2%10))
# 4번자리 472 * 8
number_4 = (number_1*((number_2%100)//10))
# 5번자리 472 * 3
number_5 = (number_1*(number_2//100))
# 6번자리
number_6 = number_1*number_2

print(number_3)
print(number_4)
print(number_5)
print(number_6)



