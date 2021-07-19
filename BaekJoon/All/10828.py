#2021.07.09
#스택
'''
import sys

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    order = command[0]
    if order == 'push':
        stack.append(int(command[1]))
    elif order == 'top':
        print(stack[-1])
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif order == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
'''
#런타임 에러

import sys

# 정수 X를 스택에 넣는 연산이다.
def push(x):
    stack.append(x)

# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    return len(stack)

# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    return 0 if stack else 1

# 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    return stack[-1] if stack else -1

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())