from typing import Sequence

class Bar:
  def __init__(self, data:Sequence[int]) -> None:
    self.data:Sequence = data
    
  def __iter__(self):
    return BarIterator(self.data)

class BarIterator:
  def __init__(self, data: Sequence) -> None:
    self.data: Sequence = data
    self.index: int = 0
    
  def __next__(self) -> int:
    if self.index < len(self.data):
      value = self.data[self.index]
      self.index += 1
      return value
    
    raise StopIteration
    
  
obj = Bar([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(obj)

for _ in obj:
  print(_)