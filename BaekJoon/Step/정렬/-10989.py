#2021.07.06
#수 정렬하기3

import sys
n = int(input())
series = [0] * 10001

for i in range(n):
  a = int(sys.stdin.readline())
  series[a] = series[a] + 1

for b in range(len(series)):
  if series[b] != 0:
    for c in range(series[b]):
      print(b)


#사실상 실패. 
#관점을 다르게 생각해야 만 풀 수 있다.