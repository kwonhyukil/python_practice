# collection -> expression, type of the elements in a collection
# list, tuple, set, dict

# x : list[int] = [1, 2, 3, 4]

# # x = [1, 2, 3, 4]

# # x = [1.1, 1.2, 1.3, 1.4]

# y : tuple[int, ...] = (1, 2, 3, 4, 5, 6)

# # y = (1, 2, 3)

# z: dict[str, str | int] = {"name" : "Hyukil", "age" : 1}

# from typing import Optional, Union, NoReturn

# o : Optional[int] = 2

# o = None

# def add_user(name:Optional[str]) -> Optional[NoReturn]:
#   if name is None:
#     raise ValueError("Name must be values")
  
  
#   print(name)

from typing import Callable, Literal, Optional, Union, NoReturn

def move(direction : Literal["forward", "backward", "left", "right"]) -> None:
  ...
  
move("forward")
move("left")
move("right")
move("backward")

def add():
  ...
# 조건 1 : 함수를 변수에 저장
x = add
# 조건 2 : 값을 읽어올 수 있어햐해
x()
# 조건 3 : 반환형으로 사용
def run(func):
  return func

run(add)



