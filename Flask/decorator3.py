# msg = "       test       "

# msg = msg.strip()
# msg = msg.upper()
# if (msg == "TEST"):
#   print("true")
# else:
#   print("false")
  
def strip(func):
  def wrapper(msg: str):
    return func(msg.strip())
    
  return wrapper

def upper(func):
  def wrapper(msg: str):
    return func(msg.upper())
    
  return wrapper

@upper
def prt_something1(msg: str): # prt_something1 = upper(prt_something1)
  print(f"prt1: {msg}")

@strip
def prt_something2(msg: str): # prt_something2 = strip(prt_something2)
  print(f"prt2: {msg}")
  
@upper
@strip
def prt_something3(msg: str): # prt_something3 = upper(strip(prt_something3))
  print(f"prt3: {msg}")
  
prt_something1("        test1       ")
prt_something2("        test2       ")
prt_something3("        test3       ")