from typing import Any, Self

class Cal:
  def __enter__(self) -> Self:
    print("Bar: enter")
    return self
  
  def div(self, x, y) -> float:
    return x / y
      
  def __exit__(self, exec_type, exec_value, traceback) -> bool:
    print(f"exit: type [{exec_type}], val: [{exec_value}], trace: [{traceback}]")
    return True
    
# obj = Bar() # -> Nothing ( 아무 일도 일어나지 않는다. )
with Cal() as obj:
  obj.div(2, 2)
  
# Bar: enter
# ---------
# Bar: exit