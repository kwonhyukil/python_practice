# 두 정수 A, B를 입력받은 다음, A+B를 출력하는 프로그램 작성

# 첫째 줄에 테스트 케이스 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.

# 각 테스트 케이스마다 "Case #x: A+B = C"형식으로 출력한다. x는 테스트 케이스 번호 1부터 시작, C는 A+B다

T = int(input())

for test in range(1,T+1):

    A, B = map(int,input().split())

    print(f"Case #{test}: {A} + {B} = {A+B}")