# 2021.09.03
# 1919
# 애너그램 만들기

ls1 = [0]*26
ls2 = [0]*26
a = input()
b = input()

for i in a:
    ls1[ord(i)-ord('a')] += 1
for i in b:
    ls2[ord(i)-ord('a')] += 1

count = 0
for i in range(26):
    count += min(ls1[i], ls2[i])

print(sum(ls1)+sum(ls2)-2*count)
