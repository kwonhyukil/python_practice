from typing import Any, Self

# python -> function -> first-class citizen

# nested function (중접)
# def out_function():
#   def in_function():
#     print("in_function")
    
#   print("out_function")
#   in_function()
  
# out_function() 

def login(func): # func에 decorator 밑에 선언한 함수(메서드)를 매개변수로 전달한다.
  def wrapper():  
    print("before login")
    func()
    print("after login")
    
  return wrapper
  
@login # 인터프리터가 코드 해석 시 해당 함수(메서드) 호출한다.
# bar = login(bar) 재 정의한다.
def bar():
  print("bar")
  
@login # 인터프리터가 코드 해석 시 해당 함수(메서드) 호출한다.
#login(foo)
def foo():
  print("foo")


#
# def out_func():
#   name = "out_func"
#   def in_func(id: int):
#     print(f"in_func: id => {id} at {name}")
    
#   return in_func

# my_func_1 = out_func()

# my_func_1(1)
# my_func_1(2)