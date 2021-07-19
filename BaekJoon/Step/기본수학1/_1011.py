#2021.06.29
#Fly me to the Alpha Centauri

n = int(input())

for _ in range(n):
    x, y = map(int,input().split())
    result = 2 #공간이동 작동 횟수
    goal = y - x - 2 #가야 하는 이동 거리

'''
1
1

2
2

3
2 1

4
2 2 

5
2 2 1 

6 
2 2 2

7
2 2 3

8
2 2 2 2

9
2 2 3 2 

10 
2 2 3 3

11
2 2 3 3 1

12
2 3 3 2 2

13
2 3 3 3 2 

14
2 3 4 3 2 

15
2 3 3 3 2 2 

'''