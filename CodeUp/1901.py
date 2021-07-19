# 2021.07.13
# (재귀 함수) 1부터 n까지 출력하기

def func(n):
    if n != 1:
        func(n-1)
    print(n)


n = int(input())
func(n)

# 이거 매우 어렵다... 생각보다 어렵다.. 재귀함수를 return 만 생각하는 습관때문인가보다
