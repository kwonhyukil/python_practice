class Bar:
    
    # Constructor ( 생성되는 객체의 주소값을 전달 받음 )
    def __init__(self, id):
        self.id = id
        # Add instance member variables
        print(f"Constructor of object {self.id} is invoked")
        
    def __del__(self):
        print(f"Destructor of object {self.id} is invoked")
        
obj1 = Bar(10)
obj2 = Bar(20)
del obj1
print("Program is termination")
del obj2