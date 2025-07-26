num1, num2 = list(map(str, input().split()))

num_list = []

num_list.append(int(num1[::-1]))
num_list.append(int(num2[::-1]))

success = max(num_list)
print(success)
