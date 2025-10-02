from functools import singledispatch

# 매개변수 1개 -> 오버로딩 구현
# 지원 자료형은 int, float

@singledispatch
def bar(x):
  raise TypeError("unsupported type")
  
@bar.register(float)
def _(x: float):
  print("float")
  
@bar.register(int)
def _(x: int):
  print("int")
  
bar(2.0)
bar("2")