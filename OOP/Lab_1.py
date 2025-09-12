class Student:
    # 학생 수
    count = 0
    
    def __init__(self, student_id, name, kor, eng, math):
        self.student_id = student_id
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = 0
        self.average = 0
        
        Student.count += 1
        
        self.id = Student.count
        
    def calc_total(self):        
        self.total = self.kor + self.eng + self.math

    def calc_average(self):
        self.average = self.total / 3
        
    def get_eng():
        pass
    
    def set_eng():
        pass

s1 = Student("2025001", "Kim", 90, 80, 85)
s2 = Student("2025002", "Lee", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()

print(f"번호:{s1.id}, 학번: {s1.student_id} 이름: {s1.name} 합계: {s1.total} 평균: {s1.average}")
print(f"번호:{s2.id}, 학번: {s2.student_id} 이름: {s2.name} 합계: {s2.total} 평균: {s2.average}")

print("총 학생 수: ", Student.count)