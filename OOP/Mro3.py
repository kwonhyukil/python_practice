class A:
    def age(self):
        print("A - age")
        print(f"A의 Mro : {A.mro()}")
        
class B(A):
    def prt(self):
        print("B - prt")
        print(f"B의 Mro : {B.mro()}")
        
class C(A):
    def name(self):
        print("C - name")
        print(f"C의 Mro : {C.mro()}")
        
class D(B, C):
    def grade(self):
        print("D - grade")
        print(f"C의 Mro : {D.mro()}")
        super().prt()
        super().name()
        super().age()

obj = D()
obj.grade()
