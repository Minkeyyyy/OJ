# 2021.09.14
# 2546
# 경제학과 정원형

n = int(input())

for _ in range(n):
    input()
    result = 0  # 평균을 올려주는 학생수
    n, m = map(int, input().split())
    c = list(map(int, input().split()))[:n]
    eco = list(map(int, input().split()))[:m]

    c_mean = sum(c) / n  # c언어 평균
    eco_mean = sum(eco) / m  # 경제학 평균

    for i in c:
        if i < c_mean and i > eco_mean:  # c언어 평균보다 낮고, 경제학 평균보다 높으면 평균을 올려주는 학생임
            result += 1
    print(result)
