from typing import Union

# def div(a : Union[int, float], b : Union[int, float]):
#   return a / b

# x = 1 # int
# y = 2.0 # float
x = "2.0"

if isinstance(x, int):
  print(f"x: {type(x)}")
elif isinstance(x, float):
  print(f"x: {type(x)}")
else:
  raise TypeError("unsupported type")