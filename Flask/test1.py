
class Bar:
  def __init__(self, name: str) -> None:
    self._name:str = name
    
  @property
  def name(self):
    return self._name + " 안녕하세요"
  
  @name.setter
  def name(self, value):
    self._name:str = value
  
obj = Bar("YC Jung")
print(obj.name)