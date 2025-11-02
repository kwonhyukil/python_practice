class Foo:
    # class member variables
    class_var = 1
    
    def __init__(self):
        # Instance member variables
        self.instance_var = 2

    # class_method 
    @classmethod
    def class_method(cls, age):
        cls.age = age
    
    # instance method
    def instance_method(self, age):
        self.age = age

obj = Foo()

obj.class_method(26)
obj.instance_method(100)

print(obj.age, Foo.age)

