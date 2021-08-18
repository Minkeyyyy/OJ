# 2021.08.19
# 1252
# 이진수 덧셈

#print(int('0b1001101', 2))
a, b = input().split()

int_a = int(('0b'+a), 2)
int_b = int(('0b'+b), 2)
int_result = int_a + int_b

print(bin(int_result)[2:])
