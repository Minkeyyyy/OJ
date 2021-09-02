# 2021.09.02
# 4766
# 일반 화학 실험

a = float(input())

while True:
    b = float(input())
    if b == 999:
        break
    print("{:.2f}".format(b-a))
    a = b
