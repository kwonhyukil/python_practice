
def is_login(func):
  
  def wrapper(msg:str, key = 20):
    print("before")
    func(msg)
    print(f"after: {key}")
  
  return wrapper

@is_login # do_something = is_login(do_something)
def do_something(msg: str):
  print(f"do something: {msg}")

# do_something = is_login(do_something)
# do_something = wrapper
# do_something 주소 값에는 wrapper이 들어가게되어
# 실질적으로 wrapper("hello")를 실행하게 된다

do_something("hello")
do_something("hi")

# def test():
#   print("test")
  
# def bar(x, y):
#   print(f"bar: {x, y}")
  
# test = bar
# test(2, 3)

def f_a(func):
  def wrapper():
    print(f"f_a: {func}")
    func()
    
  return wrapper
  
def f_b(func):
  def wrapper():
    print(f"f_b: {func}")
    func()
    
  return wrapper
  
@f_a
@f_b
def bar(): # bar = f_a(f_b(bar)) = f_a(wrapper) = wrapper
  print("bar")
  
# bar = wrapper
bar() # wrapper()