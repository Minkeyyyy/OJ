# 2021.09.06
# 5086
# 배수와 약수

while True:
    a, b = map(int, input().split())
    if a == 0 & b == 0:
        break

    if a % b == 0:
        print("multiple")  # 배수
    elif b % a == 0:
        print("factor")  # 약수
    else:
        print("neither")
