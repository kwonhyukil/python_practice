from typing import Any


class Bar:
  # 1) 생성자가 호출 될 때
  def __init__(self) -> None:
    self.name = "Bar"
    ...
    
  # event -> 객체 멤버 변수에 값을 넣을 때
  def __setattr__(self, name : str, value : Any) -> None:
    object.__setattr__(self, name, value)
    print(f"name: {name}, value: {value}")
    
  def __getattribute__(self, name: str) -> Any:
    print(f"Get: {name}")
    
obj = Bar()
# obj.bar ? 존재하지 않는다.
obj.bar = 3 # name: bar, value: 3
# obj.bar ? 존재하지 않는다.
print(obj.bar) # No attribute