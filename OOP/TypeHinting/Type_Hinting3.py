# colletion -> Abstract Data Type -> implementation Set
# Python -> list, tuple, dict, set

from typing import List

y : List = [1, 2, 3] # Legacy
x : list = [1, 2, 3]

x = (1, 2, 3)

x = {1, 2, 3}

x = {1:2, 3:4, 5:6}

def get_total_avg(x : int, y : int) -> tuple:
  sum = x + y
  avg = sum / 2
  return sum, avg

get_total_avg(2, 3)

x_tuple : tuple = (1, 2, 3)

x_tuple = [1, 2, 3]

x_dice : dict = {1:2, 3:4}

x_set : set = {1, 2, 3}

x_range : range = range(2)

x_list_int : list[int | float] = [1, 2, 3]
x_list_int = ["2", 3, 4.0]

# tuple 는 자료형, 갯수, 위치까지 정확해야함
x_tuple_int : tuple[int, float, str, int] = (2, 3.0, "2", 4)

y : tuple[int, ...] = (1, 2, 3)
y = (2, 3, 4, 5, 6)

# dict : Key 의 자료형과 Value의 자료형 지정
x_dict_str_float : dict[str, float] = {"k1" : 3.0, "k2" : 5.0}
x_dict_str_float = {1 : 2.0}

x_set_bool : set[bool] = {True, False}
