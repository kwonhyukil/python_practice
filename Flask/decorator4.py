from functools import wraps

def upper(func):
  @wraps(func)  # wrapper.__name__ = func.__name__
  def wrapper(msg:str):
    return func(msg.upper())
  
  return wrapper

@upper
def bar(msg:str): # bar = upper(bar) = bar = wrapper
  return msg
  
# bar = wrapper
# print(wraper("Hello"))
print(bar("Hello"))

print(bar.__name__)