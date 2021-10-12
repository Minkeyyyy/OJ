# 2021.10.12
# 2948
# 2009년

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yo = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]

d, m = map(int, input().split())
days = 0

for i in months[:m]:
    days += i  # 전 월까지 날짜를 더함
days += (d + 2)  # 1월 1일이 목요일이므로 index를 맞춰줌
print(yo[days % 7])
