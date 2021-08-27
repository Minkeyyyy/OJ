# 2021.08.27
# 1718
# 암호

a = input()
b = input()
flags = [ord(i) - 96 for i in b]

for ind, val in enumerate(a):
    flag = flags[ind % len(b)]
    if 96 < ord(val) < 123:
        new = ord(val) - flag
        if new < 97:
            print(chr(123-97+new), end='')
        elif new > 123:
            print(chr(96-new+122), end='')
        else:
            print(chr(new), end='')
    else:
        print(' ', end='')
