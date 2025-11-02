# Access 
# -> convention
# public -> bar
# protected -> _bar
# private -> __bar ( name mangling )

# Getter / Setter -> Method 

class A:
  def __init__(self):
    self.__age = None # -> _A__age
    
  def prt(self):
    print(self.__age)
    
# class B(A):
#   def __init__(self):
#     super().__init__()
#     self.age = 30
    
obj = A()
obj.prt()
obj._A__age = 100
print(obj._A__age)