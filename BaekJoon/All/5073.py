# 2021.09.05
# 5073
# 삼각형과 세 변

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    ls = [a, b, c]
    ls.sort()
    if ls[0] + ls[1] <= ls[2]:
        print("Invalid")
    elif ls[0] == ls[1] and ls[1] == ls[2]:
        print("Equilateral")
    elif ls[0] == ls[1] or ls[1] == ls[2]:
        print("Isosceles")
    else:
        print("Scalene")
