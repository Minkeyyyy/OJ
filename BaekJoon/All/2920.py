# 2021.10.12
# 2920
# 음계

ls = list(map(int, input().split()))
ls2 = sorted(ls)
ls3 = sorted(ls, reverse=True)

if ls == ls2:
    print("ascending")
elif ls == ls3:
    print("descending")
else:
    print("mixed")
