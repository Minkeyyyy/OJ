# 2021.07.26
# 평균 점수

sum = 0
for _ in range(5):
    score = int(input())
    if score % 5 == 0 and 0 <= score <= 100:
        if score < 40:
            sum += 40
        else:
            sum += score

print(sum//5)
