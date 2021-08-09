# 2021.08.08
# 1371
# 가장 많은 카드
import sys

alpha = [0 for i in range(97, 122+1)]
str = ''
lens = 0


def lens1(inp_str):
    if len(inp_str) > 5000:
        inp_str = inp_str[:5000]

    for i in inp_str:
        if i.isalpha():
            alpha[ord(i)-97] += 1
        else:
            continue

    max_index = max(alpha)
    for index, value in enumerate(alpha):
        if max_index == value:
            print(chr(index+97), end='')


s = sys.stdin.read()
lens1(s)
