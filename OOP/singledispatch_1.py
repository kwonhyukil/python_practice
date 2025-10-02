from functools import singledispatch

@singledispatch
def prt(x):
  raise TypeError(f"unsupported type {type(x)}")

@prt.register(int)
def _(x: int) -> str:
  return f"int {x}"

@prt.register(float)
def _(x: float) -> str:
  return f"float {x}"

print(prt(2.0))
print(prt(2))
