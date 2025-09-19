class Parent:
    
    def __init__(self):
        self.name = "Parent"
    
    def prt_name(self):
        print(self.name)
    
class Child(Parent):
    def __init__(self):
        self.name = "Child"
        super().__init__()
        
obj = Child()
obj.prt_name()
print(obj.name)