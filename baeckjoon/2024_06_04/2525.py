# 오븐시계 훈제오리구이 ~~~ 인공지능 오븐개발 ~~

# 첫째 줄에는 현재 시각이 나온다 ! 시 A , 분 B 
hour, minute = map(int,input().split())
# 두번 째줄에는 요리하는데 필요한 시간 : C 가 분단위로 주어진다.
cook_time = int(input())

# 필요한 조건 

# hour 의 값이 24를 초과 할 경우 0
# 23 48
# 25
# 0 13

# minute 의 값이 60을 이상일 경우 hour + 1
# hour + minute // 60 
# minute 의 값이 190일 경우 hour + 3 minute 10
# minute // 60 한 값(몫)을 hour에 더한다.

# minute % 60의 값(나머지)가 minute 의 값

# 23 45
# 30
# 00 15

# 23 45
# 43
# 00 28 

# minute+cook_time 의 값이 60과 같거나 초과할 경우 minute+cook_time % 60
# minute+cook_time 의 값이 60과 같거나 초과할 경우 (hour + (minute+cook_time // 60)) % 24

if hour < 24 and minute+cook_time < 60:
    print(hour, minute+cook_time)
elif hour < 24 and minute+cook_time >= 60 :
    print(((hour + ((minute+cook_time) // 60)) % 24),((minute+cook_time) % 60))
