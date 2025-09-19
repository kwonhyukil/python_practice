class Bar:
    def __init__(self):
        self.name = "Hyuk il"
        
    def prt_info(self):
        print(f"이름은 {self.name}이고, 나이는 {self.age}살 입니담.")
        
class Foo(Bar):
    def __init__(self):
        self.age = "18"
        super().__init__()
        
obj = Foo()
obj.prt_info()