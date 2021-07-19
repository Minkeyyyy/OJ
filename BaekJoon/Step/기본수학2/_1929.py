#2021.06.22
#소수 구하기

import math

def isprime(num) :
  if num == 1 : return False
  n = int(math.sqrt(num))
  for i in range(2,n+1):
    if num % i == 0:
      return False
  
  return True

s,e = map(int,input().split())

for k in range(s,e+1):
  if isprime(k) :
    print(k)