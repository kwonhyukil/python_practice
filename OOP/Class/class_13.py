class A:
  def __init__(self): # __init__ -> private 가 아니다! 
    self.public = "Public"
    self._protected = "Protected"
    self.__private = "Private"
    # self._클래스 명__변수 명
    # self._class name__variable name
    
class B(A):
  def prints(self):
    print(self.public) # public
    print(self._protected) # protected
    print(self.__private) # Error , 단 _A__private 로 접근 가능
# obj = A()

# print(obj.public) # public
# print(obj._protected) # protected
# print(obj.__private) # Error
# print(obj._A__private)

obj = B()
obj.prints()