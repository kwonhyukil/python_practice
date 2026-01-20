class Tensor:
    def __init__(self, data: list[list[float]]):
        self.data = data

    # @ 연산자 사용 시 호출되는 매직 메서드 (행렬 곱셈 구현)
    def __matmul__(self, other: "Tensor") -> "Tensor":
        W = self.data
        T = other.data
        
        # 행렬 곱셈 차원 설정
        row_W = len(W)      # 결과 행렬의 행 개수
        col_T = len(T[0])   # 결과 행렬의 열 개수
        col_W = len(W[0])   # 공통 차원 (W의 열 = T의 행)
        
        # 결과 저장용 2차원 리스트 초기화 (0.0으로 채움)
        result_data = [[0.0] * col_T for _ in range(row_W)]

        # 행렬 곱셈 알고리즘 (3중 반복문: i=행, j=열, k=내적합)
        for i in range(row_W):
            for j in range(col_T):
                for k in range(col_W):
                    result_data[i][j] += W[i][k] * T[k][j]
        
        return Tensor(result_data)

    def __repr__(self):
        return f"Tensor({self.data})"
      
    # def __str__(self) -> str:
    #   # 예: 더 예쁘게 출력하고 싶을 때
    #   return f"{self.data}"

# [실행 검증]
W = Tensor([[1.0, 2.0], [3.0, 4.0]])
T = Tensor([[5.0], [6.0]])
R = W @ T
print(R) # 출력: Tensor([[17.0], [39.0]])