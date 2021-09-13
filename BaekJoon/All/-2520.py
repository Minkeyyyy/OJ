# 2021.09.13
# 2520
# 팬케이크

mil = [8, 8, 4, 1, 9]
topping = [1, 30, 25, 10]
n = int(input())
result = []
input()

for i in range(n):
    a = list(map(int, input().split()))[:5]  # mil
    b = list(map(int, input().split()))[:4]  # topping
    if i != n-1:
        input()
    num_ban = []
    num_top = []
    for i in range(5):
        num_ban.append(int(a[i] / mil[i] * 16))
    # num_ban = [int(a[i] / mil[i] * 16) for i in range(5)]
    max_ban = max(num_ban)

    for i in range(4):
        num_top.append(b[i]//topping[i])
    # num_top = [(b[i]//topping[i]) for i in range(4)]
    sum_top = sum(num_top)
    result.append(min(sum_top, max_ban))


for i in result:
    print(i)
