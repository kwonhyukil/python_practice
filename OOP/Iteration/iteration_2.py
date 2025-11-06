class MyData:
  def __init__(self, data : list) -> None:
    self.data : list = data
    self.index = 0
    
  def __iter__(self): 
    return self
  
  def __next__(self) -> int :
    if self.index < len(self.data):
      value = self.data[self.index]
      self.index += 1
      return value
    
    raise StopIteration
    
data = MyData([1, 2, 3, 4, 5])

for x in data: 
  print(x)
  # data -> __inter__() -> self.__next__() -> 1
  # data self.__next__() -> 2
  # data self.__next__() -> 3
  # data self.__next__() -> 4
  # data self.__next__() -> 5
  # data self.__next__() -> ? 존재 안함 ( 멈춤 조건 필요 )