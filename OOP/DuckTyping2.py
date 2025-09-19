class A:
    def print_name(self):
        # self에 name 속성이 있다고 가정
        print(self.name)
        
class B:
    def __init__(self):
        self.name = "Class B"
        
class C:
    def __init__(self):
        self.name = "Class C"
        
class D:
    def __init__(self):
        # name이 아니라 title 속성만 있음
        self.title = "Class D"
        
a = A()
b = B()
c = C()
d = D()

# A.print_name()은 b, c 객체에도 그대로 적용 가능
A.print_name(b)
A.print_name(c)

# 하지만 d에는 name 속성이 없으므로 에러 발생
A.print_name(d)
# AttributeError: 'D' object has no attribute 'name'