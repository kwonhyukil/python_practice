class Bar:
    #instance method
    def i_method(self):
        self.iValue = 20
    
    #class method
    @classmethod
    def c_method(cls):
        cls.cValue = 30
        
    #staticmethod
    @staticmethod
    def s_method():
        print("s_method")
        
obj = Bar()

# obj.i_method()
obj.c_method()
obj.s_method()
Bar.i_method(obj)
del obj.iValue
del Bar.cValue
del Bar.i_method
Bar.cValue = 1000;
print(Bar.cValue)