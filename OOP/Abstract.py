# 추상화 (Abstract) -> OOP
# 미완성 + 강제 구현
# 미완성 -> 메서드 ( 자식 클래스 상속하여 구현 )

from abc import ABC, abstractmethod

# ABC -> ABstract Class
class Bar(ABC):
  @property
  @abstractmethod
  def test():
    ...
  
  @test.setter
  @abstractmethod
  def _(self, value):
    ...
    
class Foo(Bar):
  
  @property
  def test(self):
    ...
  @test.getter
  def _(self,value):
    ...

  
obj = Foo()