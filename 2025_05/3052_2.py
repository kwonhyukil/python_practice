Num_list = []

for i in range(10):
    num = int(input())
    result = num % 42

    is_running = False

    for value in Num_list:
        if result == value:
            is_running = True
            break
    
    if is_running == False:
        Num_list.append(result)

print(len(Num_list))