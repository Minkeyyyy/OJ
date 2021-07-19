#2021.06.17 성공
#부녀회장이 될테야

num = int(input())

for i in range(num):
    
    k = int(input())
    n = int(input())
    people = [[i for i in range(1,n+1)]]
    
    for ch in range(k):
        people.append([])
        for ho in range(n):
            result = 0
            result += sum(people[ch][:ho+1])
            people[ch+1].append(result)
            
    print(people[-1][-1])
