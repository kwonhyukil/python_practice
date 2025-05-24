import random

# 1. 입력값 설정
N = 10
A = 1
B = 5

# 2. 난수 생성
nums = [random.randint(A, B) for _ in range(N)]
print("난수 목록:", nums)

# 3. 등장 횟수 세기
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

# 4. 상위 3개 빈도 찾기 (동점 포함)
top = []  # [(숫자, 빈도)] 저장

for _ in range(3):  # 최대 3회
    if not freq:
        break
    max_val = max(freq.values())
    for k in list(freq.keys()):
        if freq[k] == max_val:
            top.append((k, max_val))
            del freq[k]
    if len(top) >= 3:
        break

# 5. 출력
print("가장 자주 등장한 숫자:")
for n, c in top:
    print(f"숫자 {n} → {c}회")
