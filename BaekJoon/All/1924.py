# 2021.11.12
# 1924
# 2007년

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

m, d = map(int, input().split())
cnt = 0

# 구하고자하는 달의 전 달까지의 전체 일수 합
for i in range(1, m):
    cnt += days[i-1]

# 구하고자하는 달의 날짜를 합
cnt += d

# 1월 1일이 월요일이므로 index로 계산
print(date[cnt % 7])
