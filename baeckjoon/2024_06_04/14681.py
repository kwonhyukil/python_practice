# 1사분면 + +

# 2사분면 - +

# 3사분면 - -

# 4사분면 + -

X = int(input())

Y = int(input())

if X > 0 and Y > 0:
    print("1")
elif X < 0 and Y > 0:
    print("2")
elif X < 0 and Y < 0:
    print("3")
else:
    print("4")