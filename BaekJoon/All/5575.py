# 2021.07.25
# 타임 카드

for _ in range(3):
    s_h, s_m, s_s, e_h, e_m, e_s = map(int, input().split())
    r_h, r_m, r_s = 0, 0, 0

    if e_s < s_s:
        e_m -= 1
        r_s = e_s - s_s + 60
    else:
        r_s = e_s - s_s

    if e_m < s_m:
        e_h -= 1
        r_m = e_m - s_m + 60
    else:
        r_m = e_m - s_m

    if e_h < s_h:
        print("error")
    else:
        r_h = e_h - s_h

    print(r_h, r_m, r_s)
