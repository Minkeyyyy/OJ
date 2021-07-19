#2021.06.21
#소수

m = int(input())
n = int(input())
list1 = []

for i in range(m, n+1) :
  check = 0 
  for j in range(1, i+1):
    if i % j == 0:
      check += 1
    if check > 2:
      break
  if check == 2:
    list1.append(i)

if list1:
  print(sum(list1))
  print(min(list1))
else:
  print(-1)