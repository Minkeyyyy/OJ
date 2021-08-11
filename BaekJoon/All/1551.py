# 2021.08.11
# 1551
# 수열의 변화

n, k = map(int, input().split())
flst = list(map(int, input().split(',')))[:n]
# 새로운 수열을 만들어서 리스트로 반환


def sooy(lst):
    new_lst = []
    for i in range(0, len(lst)-1):
        new_lst.append(lst[i+1]-lst[i])
    return new_lst


# 횟수만큼 새로운 수열을 만듬
for i in range(k):
    flst = sooy(flst)
# join함수를 사용하기 위해 숫자들을 문자열로 변환
flst = map(str, flst)

print(','.join(flst))
