# 2021.10.28
# 3448
# 문자 인식

n = int(input())
count = 0

for _ in range(n):
    texts = ""
    while True:
        text = input()
        if text == "":
            num = (len(texts)-texts.count('#'))/len(texts)*100
            if num.is_integer():
                print("Efficiency ratio is {}%.".format(int(num)))
            else:
                num = round(num, 1)
                print("Efficiency ratio is {}%.".format(num))
            break
        else:
            texts += text

# 틀림.
