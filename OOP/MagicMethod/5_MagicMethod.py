from typing import Any, Self

from dataclasses import asdict, dataclass, field

@dataclass
class Student: # data 저장용 클래스가 된다
  id: str   = field(default="2")    # 인스턴스 멤버변수
  name: str = field(compare = False, repr=False)    # 인스턴스 멤버변수
  age: int     # 인스턴스 멤버변수
  
  data:list = field(default_factory=[])
  
  def __eq__(self, value: "Student") -> bool:
    return self.id == value.id
  
  # <=
  def __le__(self, value: "Student") -> bool:
    return self.age <= value.age
  
std1 = Student("123", "KIm", 20)
std2 = Student("123", "Lee", 10)
  
print(std1)
print(std2.name, std2.id, std2.age)
print(asdict(std1))

print(std1 <= std2)