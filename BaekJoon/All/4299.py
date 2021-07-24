# 2021.07.24
# AFC 윔블던

plus, minus = map(int, input().split())

if plus - minus < 0 or minus - plus > 0 or (plus - minus) % 2 != 0:
    print(-1)
else:
    a = (plus - minus) // 2
    b = plus - a
    print(max(a, b), min(a, b))

#은근히 수학적인 부분이 많다.