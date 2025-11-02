# Colletion -> Abstract Data Type -> Implementation Set
# Python -> list, tuple, dict. set

from typing import Sequence, Union

# Squence -> Type hinting -> list, tuple, range

x_squence_int : Sequence[int] = [1, 2, 3]
x_squence_int = (1, 2, 3)

x_squence_int = {1, 2, 3}
x_squence_int = {1:2, 3:4, 5:6}

# Union -> 집합의 원소 중 하나이면 -> Ok, 모두 해당하지 않으면 -> Error

# 구버전
x: Union[int, float, bool]
# 최신 버전
x_new : int | float | bool

x = 2
x = 3.0
x = False
x = "2.0"

