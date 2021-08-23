# 2021.08.21
# 1672
# DNA 해독

n = int(input())
y = input()
chat = ['A', 'G', 'C', 'T']
results = ['A', 'C', 'A', 'G', 'C', 'G', 'T',
           'A', 'A', 'T', 'C', 'G', 'G', 'A', 'G', 'T']

# 해당 list의 결과를 알기 위한 함수


def change(two):
    # 문자열 두 중에 앞의 것의 index에 *4를 해주고
    result = int(chat.index(two[0])*4)
    # 뒤의 것에 index를 더하면 겹치지 않는 result가 나옴
    result += int(chat.index(two[1]))
    # 결과물 index로 results의 value를 가져오면 다음 염기가 구해짐
    return results[result]


while True:
    if len(y) == 1:
        print(y)
        break
    # 뒤에 두 문자만 잘라서 change함수에 대입해서 다음 염기로 치환
    changed = change(y[-2:])
    y = y[:-2]+changed
