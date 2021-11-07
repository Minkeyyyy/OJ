# 2021.11.07
# 9366
# 삼각형 분류

for i in range(int(input())):
    ls = list(map(int, input().split()))
    ls.sort()
    if ls[2] >= ls[0]+ls[1]:
        print(f"Case #{i+1}: invalid!")
    else:
        if ls[0] == ls[1] == ls[2]:
            print(f"Case #{i+1}: equilateral")
        elif ls[0] == ls[1] or ls[1] == ls[2]:
            print(f"Case #{i+1}: isosceles")
        else:
            print(f"Case #{i+1}: scalene")
