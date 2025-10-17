class Student:
  __id_count = 0
  
  def __init__(self, name, id, gender):
    self.name = name
    self.id = Student.__id_count
    self.gender = gender
    Student.__id_count += 1
    
    self.total = 0
    self.avg = 0.0
       
  def set_score(self, korean, math, eng):
    self.grade_korean = korean
    self.grade_math = math
    self.grade_eng = eng
    self.total = korean + math + eng
    self.avg = self.total / 3
      
  def get_total_avg(self):
    return f"total: {self.total}, avg: {self.avg}"
  
  @classmethod
  def get_id_count(cls):
    return f"현재 생성된 객체: {cls.__id_count}개"
  
  @staticmethod
  def get_avg(arg1, arg2, arg3):
    return (arg1 + arg2 + arg3) / 3

# 객체 생성
s1 = Student("Alice", 0, "F")
s2 = Student("Bob", 0, "M")

# 점수 입력
s1.set_score(90, 85, 92)
s2.set_score(75, 80, 78)

# 총점과 평균 출력
print(s1.get_total_avg())
print(s2.get_total_avg())

# 클래스 메서드 호출 ( 현재 생성된 객체 수)
print(Student.get_id_count())

# 정적 메서드 호출 (별도의 객체 없이 평균 계산)
print(Student.get_avg(100, 90, 80))