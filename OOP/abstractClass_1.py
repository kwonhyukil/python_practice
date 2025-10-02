from abc import ABC,abstractmethod

# 추상클래스를 정의
# Java -> abstract class Bar{ }

# Bar를 추상클래스로 정의
class Bar(ABC):
  
  # 추상 인스턴스 메서드 정의
  @abstractmethod
  def instance_method(self):
    pass

class MyClass(Bar):
  def instance_method(self):
    print("MyClass : instance_method")

obj = MyClass()
obj.instance_method()