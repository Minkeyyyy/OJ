# 2021.07.26
# 체스판 다시 칠하기

n, m = map(int, input().split())
wrong = 0

for i in range(n):
    inp = input()
    if i == 0:
        start = inp[0]
