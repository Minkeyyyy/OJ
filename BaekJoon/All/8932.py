# 2021.10.27
# 8932
# 7종 경기

def track(a, b, c, p):
    return int(a*((b-p)**c))


def field(a, b, c, p):
    return int(a*((p-b)**c))


n = int(input())

for _ in range(n):
    ls = list(map(int, input().split()))
    result = track(9.23076, 26.7, 1.835, ls[0]) + field(1.84523, 75, 1.348, ls[1])+field(56.0211, 1.5, 1.05, ls[2])+track(4.99087, 42.5, 1.81, ls[3])+field(
        0.188807, 210, 1.41, ls[4]) + field(15.9803, 3.8, 1.04, ls[5]) + track(0.11193, 254, 1.88, ls[6])

    print(result)
