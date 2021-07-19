#2021.07.05
#수열의 합

n, l = map(int,input().split())
list1 = [i for i in range(1,100+1)]

mini = n // (l+2)
for i in range(mini, 1000000000+1):
    new = list1[i:i+l+1]
    list_sum = sum(new)
    if list_sum <= n :
        if list_sum == n:
            for j in new:
                print(j,  end =' ')
    else:
        print(-1)
        break