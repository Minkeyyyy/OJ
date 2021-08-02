# 2021.08.02
# 과목선택

scores = []
for _ in range(6):
    scores.append(int(input()))

science = sorted(scores[:4])
result = sum(science[1:]) + max(scores[4], scores[5])

print(result)
