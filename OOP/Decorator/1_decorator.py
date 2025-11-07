from typing import Any, Self

def bar(func):
  def wrapper(msg : str):
    print("write log")
    func(msg)

  return wrapper

@bar # bar(test)
def test(msg): # test = bar(test)
  print(msg)
  
test("hello")
print(test.__name__)