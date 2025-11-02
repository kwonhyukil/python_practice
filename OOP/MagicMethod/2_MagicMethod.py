from collections.abc import Iterable


class Bar:
  def __str__(self) -> str:
    return f"Bar"

obj = Bar()

print(obj)

class Student:
  def __init__(self, id : int) -> None:
    self.id : int = id
    self.kor : int = 0
    self.eng : int = 0
    self.math : int = 0
  
  def __call__(self, kor: int, eng: int, math: int ): 
    self.kor = kor
    self.eng = eng
    self.math = math
    
  def __iter__(self):
    yield self.kor
    yield self.eng
    yield self.math
      
  def __str__(self) -> str:
    return f"국어 점수: {self.kor} 영어 점수: {self.eng} 수학 점수: {self.math}"
  
  def __eq__(self, value: "Student") -> bool:
    return (self.id == value.id)
    
std1 = Student(1)
std2 = Student(2)

# std1.__eq__(std2)
# std1.id == std2.id 
print(std1 == std2)

obj = Student(1)
obj(10, 20, 30)
print(obj)

for score in obj:
  print(score)