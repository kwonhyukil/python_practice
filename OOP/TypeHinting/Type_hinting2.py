# a : None = None

a = 1
a = 2.0
a = "3.0"

def somthing(a : int , b : float , c : None=None) -> None:
  ...

# Callabel(param...) -> return type
def sum(x : int, y : int ) -> None:
  print( x + y )
  
class Bar:
  # 생성자 반환 x
  def __init__(self, x: int, y : str) -> None:
    self.x : int = x
    self.y : str = y