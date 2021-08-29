# 2021.08.29
# 4493
# 가위 바위 보?

n = int(input())  # 전체 케이스
rps = ['R', 'P', 'S']
scores = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

for _ in range(n):
    result = 0
    m = int(input())  # 가위바위보 횟수
    for _ in range(m):
        a, b = input().split()
        result += scores[rps.index(a)][rps.index(b)]

    if result > 0:
        print('Player 2')
    elif result < 0:
        print('Player 1')
    else:
        print('TIE')
