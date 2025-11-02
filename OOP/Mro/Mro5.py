class A:
    name = "A"
    
    def __init__(self):
        print(f"B의 age : {self.age}")
        self.age = 20
        print(f"A의 age : {self.age}")
        
class B(A):
    name = "B"
    
    def __init__(self):
        self.age = 100
        print("B의 나이 100 살")
        super().__init__()
        
obj = B()
print(obj.age)