#2021.06.17
#ACM 호텔

n = int(input())
for _ in range(n):
    h,w,n = map(int,input().split())
    # if 1 <= n <=(h*w):
    #     ho = n // h  + 1 
    #     ch = n - (ho-1)*h
    #     print(ch*100+ho)
    
    if n%h == 0:
        ho = n // h
        ch = h
    else:
        ch = n%h
        ho = n // h + 1
    print(ch*100 + ho)