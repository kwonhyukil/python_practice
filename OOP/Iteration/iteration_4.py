def bar():...
def test():
  yield 1
  yield 2
  yield 3
  yield 4
  
obj = test()

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

def my_range(num:int):
  count:int = 0
  
  while (count < num):
    yield count
    count += 1
    
for x in my_range(5):
  print(x)