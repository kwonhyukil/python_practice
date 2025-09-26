# def prt(positional, variable prositional, keyword, \
#         variable keywords):
#   ...

# def prt(a, b = 2, c = 3, d):
#   print(a, b, c)
  
# prt(1)
# prt(10, 20)  
# prt(2, 3)
# prt(b = 3, a = 2) # Keyword 사용하여 매개변수 
# / : 위치기반 매개변수 전용 -> 
# / 앞까지의 모든 매개변수는 위치기반 인자값으로 할당되어야 된다

from typing import Union

def calculate (x : Union[int, float], y : Union[int, float], op = "+"):
  if op == "+":
    print(x + y)
  elif op == "-":
    print(x - y)
  else:
    print("error")

calculate(2, 3)
calculate(10, 20, "-")

# 가변 위치 인자
# def prt(a, *arg):
#   print(a, arg)
  
# prt(1)
# prt(1, 2)
# prt(1, 2, 3)

# 가변 키워드
# def prt(**arg):
#   for key, value in arg.items():
#     print(key, value)
  
# prt(a = 2)
# prt(d = 3, test = "ddd")

def prt(a, *b, c = 10, d = 20, **kwargs):
  print(a, b, c, d, kwargs)
  
prt(1, 2, 3, 4, 5, op = 200, d = 100)


def prt(pp, *vpp, kp, **vkp):
  pass