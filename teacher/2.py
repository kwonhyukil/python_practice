import random

random_list = []

for i in range(0, 20):
    random_value = random.randint(0, 100)
    random_list.append(random_value)
print(len(random_list))
print(random_list)

value_list = {}

for _ in range(0, 21, 5):
    if _ == 5:
        value_list['1'] = random_list[:5]
    if _ == 10:
        value_list['2'] = random_list[5:10]
    if _ == 15:
        value_list['3'] = random_list[10:15]
    if _ == 20:
        value_list['4'] = random_list[15:20]
print(value_list)

def menu():
    print("="*3 + "리스트 관리 프로그램" + "="*3 )
    print("1. 각 리스트 내 데이터 출력")
    print("2. 특정 리스트 출력")
    print("3. 특정 리스트 삭제")
    print("4. 프로그램 삭제")

edit_list = {}

while True:
    
    menu()

    num = []
    select = int(input("메뉴 선택: "))
    # num = [i for i in range(len(value_list))]
    # print(num)
    if select == 1:
        for i in range(len(value_list)):
            # print(type(i))
            print(f"[리스트 {i + 1}]: ", value_list[str(i + 1)])
    if select == 2:
        print_list_num = str(input(f"출력할 리스트 번호(1 ~ {len(value_list)}): "))
        if 0 < int(print_list_num) < len(value_list) + 1:
            print(f"[리스트{print_list_num}]: {value_list[print_list_num]}")
        else:
            print("리스트 번호가 범위를 벗어났습니다.")
    if select == 3:
        delect_list_num = str(input(f"삭제할 리스트 번호(1 ~ {len(value_list)}): "))
        if 0 < int(delect_list_num) <= len(value_list):
            del[value_list[delect_list_num]]
            num.append(delect_list_num)
        print(f"리스트 {delect_list_num}가 삭제되었습니다.")
        
        for i in value_list:
            
            
    if select == 4:
        print("프로그램 종료")
        break
    # print(value_list)