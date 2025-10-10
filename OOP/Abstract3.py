# 아 ~~~~~~~~~~~~~~~~~~~~~
# 동적 타이핑 언어가 좋아... 근데 ... 코드의 규모가 커질수록 ... 관리의 어려움이 있다.
# Type hinting -> 동적인 언어
# "체크 포인트" -> 동적인 언어의 특성을 바꾸진 못해 ()
from typing import Union

# Union Ver
# def sum(a : Union[int, float], b : Union[int, float]) -> int | float:
def sum(a : int | float, b : int | float) -> int | float:
  return a / b

print(sum(1, 1)) # 2
print(sum(1, 1.0)) # 2.0
print(sum("1", "1")) # 11