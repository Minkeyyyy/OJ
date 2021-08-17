# 2021.08.16
# 16199
# 나이 계산하기

birth = list(map(int, input().split()))
st = list(map(int, input().split()))
# 만 나이
if st[1] > birth[1]:
    result1 = st[0] - birth[0]
elif st[1] == birth[1]:
    if birth[2] <= st[2]:
        result1 = st[0] - birth[0]
    else:
        result1 = st[0] - birth[0] - 1
else:
    result1 = st[0] - birth[0] - 1
# 세는 나이
result2 = st[0] - birth[0] + 1
# 연 나이
result3 = st[0] - birth[0]

print(result1)
print(result2)
print(result3)
