# 2021.10.22
# 3059
# 등장하지 않는 문자의 합

n = int(input())

for _ in range(n):
    # 모든 알파벳 index를 True로 초기화
    checks = [True]*26
    s = input()
    for i in s:
        idx = ord(i)-65
        # 알파벳이 아직 안나왔으면 False
        if checks[idx]:
            checks[ord(i)-65] = False

    result = 0
    for i in range(26):
        # 알파벳이 등장하지 않았으면 아스키코드 합
        if checks[i]:
            result += i + 65

    print(result)
