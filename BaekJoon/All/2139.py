# 2021.11.29
# 2139
# 나는 너가 살아온 날을 알고 있다

from datetime import datetime

while True:
    s = input()
    if s == '0 0 0':
        break
    s = s.split()
    new = datetime.strptime(s[2]+s[1]+s[0], "%Y%m%d")
    past = datetime.strptime(s[2]+"0101", "%Y%m%d")
    date_diff = new - past

    print(date_diff.days+1)
