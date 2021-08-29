# 2021.08.20
# 1592
# 영식이와 친구들

n, m, l = map(int, input().split())
counts = [0] * (n+1)  # 개인당 공을 받은 횟수 기록
result = 0  # 전체 횟수 기록
now = 1

while True:
    # 지금 현재 있는 곳의 횟수 1증가
    counts[now] += 1
    if counts[now] == m:
        break
    else:
        # 짝수라면 반시계 방향으로 l만큼
        if counts[now] % 2 == 0:
            now -= l
            result += 1
            if now <= 0:
                now = n+now
        # 홀수라면 시계방향으로 l만큼
        else:
            now += l
            result += 1
            if now > n:
                now = now - n
print(result)
