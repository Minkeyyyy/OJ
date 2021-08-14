# 2021.08.13
# 2721
# 삼각수의 합
t_list = []


def t(num):
    if (len(t_list)-1) < num:
        for i in range(len(t_list), num + 1):
            sum1 = 0
            for j in range(1, i+1):
                sum1 += j
            t_list.append(sum1)
    else:
        return


def wei(num):
    result = 0
    for i in range(1, num+1):
        result += i*(t_list[i+1])
    return result


n = int(input())

for _ in range(n):
    case = int(input())
    t(case+1)
    print(wei(case))

# 2021.08.13
# 2721
# 삼각수의 합

# n = int(input())

# for _ in range(n):
#   num = int(input())
#   result = 0
#   for i in range(1,num+1):
#     result += i*sum(range(i+2))
#   print(result)
