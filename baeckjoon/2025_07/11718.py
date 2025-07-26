import sys

for line in sys.stdin:
    print(line, end='')


while True:
    try:
      a = input()
      print(a)
    except:
       break
    finally:
       print("메롱")