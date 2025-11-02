def test(x : int, y : float, z : str) -> str:
  return f"x: {x} y: {y}, z: {z}"
  
from typing import Callable
# my_func -> argument -> 3개, 반환형은 문자열
# Callable[매개변수 자료형, 반환값 자료형]
# Callable[[매개변수1 자료형, 매개변수2 자료형 ...], 반환값 자료형]
def run(my_func : Callable[[int, float, str], str], a : int, b : float, c : str) -> None:
  
  print(my_func(a, b, c))
  
# test 함수를 run 함수의 매개변수를 할당한다.
run(test, 1, 2, 3)

def test_2(x : str, y : float) -> None:
  ...
  
  
run(test_2, 1, 2, 3)