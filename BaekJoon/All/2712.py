# 2021.09.26
# 2712
# 미국 스타일

inp = ['kg', 'lb', 'l', 'g']
num = [2.2046, 0.4536, 0.2642, 3.7854]
out = ['lb', 'kg', 'g', 'l']

n = int(input())

for _ in range(n):
    a, b = input().split()
    a = float(a)

    idx = inp.index(b)
    result = a*num[idx]
    print("{:.4f} {}".format(result, out[idx]))
