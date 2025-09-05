class Foo:
    name = "Class member variable: Foo"
    # 1. 생성자
    # 2. 멤버 속성 (Attribute)
    # 3. 멤버 메소드
    def test(instance_ref):
        instance_ref.name = "Instance member variable: "
    # 4. 소멸자 -> 쓰레기 수집자 도입
    #   -> 사용하지 않는 객체 삭제
    #   -> 메모리 릭(leak) 누수
    pass

obj = Foo()
obj.test()

print(obj.name)
print(Foo.name)