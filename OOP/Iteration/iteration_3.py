class Mydata:
  def __init__(self, data : list) -> None:
    self.data : list = data
    
  def __iter__(self):
    return BarInterator(self.data)
      
class BarInterator:
  def __init__(self, data) -> None:
    self.data = data
    self.index: int = 0
    
  def __next__(self) -> int:
    if self.index < len(self.data):
      value = self.data[self.index]
      self.index += 1
      return value
    
    raise StopIteration
    
obj = Mydata([1, 2, 3, 4, 5, 6, 7])

print(obj)

for _ in obj:
  print(_)