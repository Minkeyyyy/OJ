#2021.06.11
#크로아티아 알파벳

unusual = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inp = input()

for uns in unusual:
    if uns in inp:
        inp = inp.replace(uns, '1')

print(len(inp))