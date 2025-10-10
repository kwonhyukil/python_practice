class Bar:
  # 반드시 자식 클래스에서 구현되기를 바란다
  def test(self):
    raise NotImplementedError
  
class Foo(Bar):
  ...
  

obj = Foo() # -> 객체 생성 O
obj.test()