# 2021.07.13
# [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기

jumin = input()

if len(jumin) == 14 and jumin[:6].isdigit() and jumin[6] == '-' and jumin[7:].isdigit():
    print(jumin[:6] + jumin[7:])
