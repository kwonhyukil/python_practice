# Optional -> if else -> if [T] else None

from typing import Optional, Literal, Any

x_opt_int : Optional[int]

x_opt_int = 3
x_opt_int = None
x_opt_int = 3.0
x_opt_int = "4"

# literal : 안에 값을 명시하여 해당 값이 아니면 Error 
x_literal : Literal[1, 2, 3]
x_literal = 4

# man, woman 의 값이 아니면 Error
gender : Literal["man", "woman"]
gender = "man"
gender = "woman"
gender = "123"

# Any : 모든 것을 다 받을 수 이써요 ( 가능한 안쓰는 편이 좋다. )
x: Any
x = 1
x = 2.0
x = "2"
x = True

