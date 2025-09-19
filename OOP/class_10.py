class Bar:
    # 멤버 변수 ( 속성 ) -> 1. 인스턴스 멤버 변수, 2. 클래스 멤버 변수
    
    # 클래스 멤버 변수
    # 실무 >_< 여기
    classVariable = 100
    
    def __init__(self):
        # 초기화 작업
        # 인스턴스 멤버 변수 : 실무 >_< 여기
        instanceVariable = 220
        print("생성자 호출")
        
    # 메서드 -> 멤버 메서드 ( 인스턴스, 클래스 ), 스태틱 (static) 메서드
    
    # 멤버 메서드 ->
    # 1. 인스턴스 메서드 : 각 객체의 인스턴스 멤버 변수 ( self )
    def instance_method(self):
        pass
    
    # 2. 클래스 메서드 : 인스턴스들끼리 공유되는 변수( cls ), 
    @classmethod
    def class_method(cls):
        pass
    
    # 3. 스태틱 메서드 : 독립적으로 동작
    @staticmethod
    def static_method():
        pass
        
    def __del__(self):
        # 객체 소멸 전 자원 정리
        pass
    
obj = Bar()