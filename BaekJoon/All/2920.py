# # 2021.10.12
# # 2920
# # 음계

# ls = list(map(int, input().split()))
# ls2 = sorted(ls)
# ls3 = sorted(ls, reverse=True)

# if ls == ls2:
#     print("ascending")
# elif ls == ls3:
#     print("descending")
# else:
#     print("mixed")

# 2022.02.11
# 2920
# 음계
 
ls = list(map(int,input().split()))
ascending = True
descending = True

for i in range(1,8):
    if ls[i] < ls[i-1]:
        ascending = False
    elif ls[i] > ls[i-1]:
        descending = False
    else:
        continue
    
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")