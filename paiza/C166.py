price = int(input())

coin_list = [500, 100, 50, 10, 5, 1]
coin_count = 0

for i in coin_list:

    coin_count += price // i
    price = price % i

print(coin_count)