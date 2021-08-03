# 2021.08.03
# 14470
# 전자레인지

inp = []
result = 0

for _ in range(5):
    inp.append(int(input()))

if inp[0] < 0:
    result += inp[2] * (-inp[0]) + inp[3] + inp[-1] * (inp[1])
else:
    result += inp[-1] * (inp[1] - inp[0])

print(result)
