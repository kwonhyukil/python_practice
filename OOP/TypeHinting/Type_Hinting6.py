# Callable -> 함수, 메서드

from ast import Call
from typing import Callable

def sum(x : float, y : float) -> float:
  return x + y

# 1급 시민
sum_2 = sum
print(sum_2(2, 3)) # 5

def do_something(x : float, y : float, op : Callable[[int | float, int | float], int | float]):
  return op(x, y)

# op : 함수 
# 매개변수의 갯수와 자료형, 반환형이 중요하다
print(do_something(1, 2, sum))

