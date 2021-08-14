# 2021.08.08
# 1371
# 가장 많은 카드
import sys

#알파벳을 모두 넣어줌
alpha = [0 for i in range(97, 122+1)]

def lens1(inp_str):
    if len(inp_str) > 5000: 
        inp_str = inp_str[:5000]

    for i in inp_str:
        if i.isalpha(): #알파벳이면 해당 index의 값을 하나 증가
            alpha[ord(i)-97] += 1
        else:
            continue

    max_index = max(alpha) #가장 많이 나온 알파벳의 횟수 지정
    for index, value in enumerate(alpha):
        if max_index == value: #횟수가 가장 많은 것이면 출력
            print(chr(index+97), end='')


s = sys.stdin.read()
lens1(s)
