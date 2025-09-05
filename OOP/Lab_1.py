class Student:
    
    # 학생 수
    count = 1
    
    def __init__(self, student_id, name, eng, kor, math):
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
        
    def calc_total(self, eng, kor, math):
        self.eng = eng
        self.kor = kor
        self.math = math
        self.total = self.kor + self.eng + self.math
 
    
    def calc_average(self, total):
        self.total = total
        self.average = total / 3

    
    
s1 = Student("2025001", "Kim", 90, 80, 85)
s2 = Student("2025002", "Lee", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()

print(s1.id, s1.name, s1.total, s1.average)
print(s2.id, s2.name, s2.total, s2.average)