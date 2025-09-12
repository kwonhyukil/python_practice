class Foo:
    name = "Class Object"
    
    
    
obj = Foo()

obj.name = "Foo instance"

print(obj.name)

print(Foo.name)