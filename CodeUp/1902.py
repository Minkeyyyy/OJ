# 2021.07.13
# (재귀 함수) 1부터 n까지 역순으로 출력하기

n = int(input())


def func(n):
    print(n)
    if n != 1:
        func(n-1)


func(n)
