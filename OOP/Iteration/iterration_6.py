from typing import Any


class Bar:
  def __init__(self):
    self.name = "Bar"
    
  def __setattr__(self, name: str, value: Any) -> None:
    object.__setattr__(self, name, value)
    print(f"name: {name}, value: {value}")
    
  def __getattribute__(self, name: str) -> Any:
    try:
      value = object.__getattribute__(self, name)
      print(f"Get: {name}")
      return value
    except AttributeError:
      print(f"MISSING: {name}")
      
obj = Bar()
print(obj.tag)
obj.new = 2