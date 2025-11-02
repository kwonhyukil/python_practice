class Bar():
  
  def __init__(self, name : str, age : int) -> None:
    self.name : str = name
    self.age : int = age
    
from typing import Any

x: int | float = 1

from typing import Union

y: Union[int, float] = 2