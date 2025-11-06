from typing import ClassVar

class Student:
  # name:str
  # id:str
  # age:int
  
  # count:ClassVar[int]
  
  def __init__(self, name : str, id : str, age : int) -> None:
    self.name = name
    self.id = id
    self.age = age
    

# class MyDataset:
#   def __init__(self, feature : list, label : list) -> None:
#     self.feature : list = feature
#     self.label : list = label
    
#   def __str__(self):
#     return f"Dataset: \n feature: {self.feature} \
#       \n label: {self.label}"
    
#   def __repr__(self):
#     return "For log, debug and Doc"
  
#   def __getitem__(self, index : int) -> tuple:
#     return self.feature[index], self.label[index]
  
#   def __setitem__(self, index : int, value : tuple[list, list]) -> None:
#     self.feature[index] = value[0]
#     self.label[index] = value[1]
    
#   def __len__(self):
#     return len(self.feature)
  
#   def __next__(self) -> int:
#     yield
    
# dataset = MyDataset([1, 2, 3], [10, 20, 30])

# for x, y in dataset:
#   print("x, y: {x}, {y}")
  
class MyDataset:
  def __init__(self, feature : list, label : list) -> None:
    self.feature : list = feature
    self.label : list = label
  
  # yield 가 있으면 generator 객체로 바뀐다.
  def __iter__(self):
    for x, y in zip(self.feature, self.label):
      yield x, y
    
dataset = MyDataset([1, 2, 3], [10, 20, 30])

for x, y in dataset:
  print(f"x, y: {x}, {y}") 