from typing import Union
# type hinting

x : int = 3


def div(a : Union[int, float] , b : Union[int, float]): # a = int , b = int -> float
  return (a / b)

print(4 / 2)
print(4.0 / 2.0)
# print("4" / "2")

print(div(4, 2))
print(div(4.0, 2.0))
print(div("4", "2"))