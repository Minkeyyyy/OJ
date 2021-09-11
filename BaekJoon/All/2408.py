# 2021.09.11
# 2408
# 큰 수 계산
import math

n = int(input())
st = ""
flag = False

for _ in range(2*n - 1):
    inp = input()
    if inp == '/':
        st += '//'
    else:
        st += inp

print(eval(st))


# n = int(input())
# nums = []
# oper = []
# new = []

# result = ""


# for _ in range(2*n):
#     inp = input()
#     if inp.isdigit():
#         nums.append(int(inp))
#     else:
#         oper.append(inp)

# for idx, val in enumerate(oper):
#     if val == '*':
#         result += str(nums[idx] * nums[idx+1])
#     elif val == '/':
#         result += str(math.floor(nums[idx] / nums[idx+1]))
#     else:
#         result += str(nums[idx]) + val
