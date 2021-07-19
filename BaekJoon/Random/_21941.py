#2021.06.18
#문자열 제거

import sys

input_string = sys.stdin.readline()
n = int(sys.stdin.readline())
erase = {}
total_score = 0

for _ in range(n):
    string, score = sys.stdin.readline().split()
    score = int(score)
    erase[string] = score

erase2 = sorted(erase.values())
print(erase2)
for sc in erase2:
    string = erase()
    if erase[string] > len(string):
        while string in input_string:
            input_string = input_string.replace(string,'_'*len(string), 1)
            total_score += erase[string]
            #print(total_score)
print(input_string)
input_string2 = input_string.replace('_', '').strip()

total_score += len(input_string2)
print(total_score)