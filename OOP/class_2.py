class Foo:
    
    def set_name(self, name):
        self.name = name

    
    def set_age(self, age):
        print(age)
    
obj = Foo()

# Foo.set_name(obj, "Hong")
obj.set_name("Hong")
print(obj.name)

obj.set_age(42244224)