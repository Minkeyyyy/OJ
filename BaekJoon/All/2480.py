# 2021.07.18
# 주사위 세개

numbers = list(map(int, input().split()))
set_numbers = set(numbers)

if len(set_numbers) == 1:
    print(numbers[0] * 1000 + 10000)
elif len(set_numbers) == 2:
    if numbers.count(numbers[0]) == 2:
        print(1000+numbers[0]*100)
    elif numbers.count(numbers[1]) == 2:
        print(1000+numbers[1]*100)
else:
    print(max(numbers)*100)
