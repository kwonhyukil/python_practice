class student:
    school = "YJU"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}, {self.age} years old.")
    
    @classmethod
    def get_school(cls):
        print("School: ", cls.school)
        
    @staticmethod
    def hello():
        print("Hello, Python OOP!")