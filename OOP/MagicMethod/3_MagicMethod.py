from typing import Sequence

class Bar:
  def __init__(self, data: Sequence[int]) -> None:
    self.data: Sequence[int] = data
    self.index:int = 0

  def __len__(self) -> int:
    return len(self.data)
  
  def __iter__(self):
    print("iter is invoked")
    return iter(self.data)
  # return self.data.__iter__()
  # yield from self.data
  
  def __next__(self) -> int:
    # self.data 리스트의 0번째 요소에서 마지막 요소까지 순회
    if self.index < len(self.data):
      value = self.data[self.index]
      self.index += 1
      return value
    
    else:
      self.index = 0
      raise StopIteration
          
obj = Bar([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(len(obj))

for _ in obj:
  print(_)
  
for _ in obj:
  print(_)
  
x = [10, 20, 30, 40, 50]

for _ in x:
  print(_)
  
foo = iter(x)
while True:
  try:
    next(foo)
  except StopIteration:
    break