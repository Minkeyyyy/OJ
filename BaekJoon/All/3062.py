# 2021.10.22
# 3062
# 수 뒤집기

n = int(input())

for _ in range(n):
    num = input()
    re_num = num[::-1]
    int_num = int(num)
    int_re_num = int(re_num)
    sum1 = int_num + int_re_num
    str_sum1 = str(sum1)
    # 더한 것이 앞뒤로 대칭인지 알기 위한
    count = 0

    for i in range(len(str_sum1)//2):
        # 앞과 뒤가 대칭이면 count 1증가
        if str_sum1[i] == str_sum1[len(str_sum1) - i - 1]:
            count += 1
    # 길이의 절반과 count가 같으면 출력
    if count == len(str_sum1)//2:
        print('YES')
    else:
        print('NO')
