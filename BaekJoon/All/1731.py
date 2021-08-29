# 2021.08.29
# 1731
# 추론

n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))

#1번 2번항 공차
cha1 = ls[1] - ls[0]
if (ls[1] % ls[0]) == 0:
    #1번 2번항 공비
    bi1 = ls[1]//ls[0]
    if (ls[2] // ls[1]) == bi1:
        #등비수열인 것이 확정
        print(ls[-1]*bi1)
else:
    #등차수열인 것이 확정
    print(ls[-1] + cha1)
