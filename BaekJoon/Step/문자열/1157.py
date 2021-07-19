#단어 공부

inp = input()
inp = inp.upper()
count = [0 for i in range(26)]

for i in inp:
    index = ord(i) - 65 
    count[index] += 1

count_check = sorted(count)

if count_check[-1] == count_check[-2]:
    print('?')
else:
    max_index = count.index(max(count))
    print(chr(max_index+65))
