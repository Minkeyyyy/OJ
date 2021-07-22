#2021.07.22
#저항

'''
dic = {'black' : 0, 'brown': 1, 'red' : 2,
'orange' : 3 , 'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet':7,
'gray' : 8 , 'white' : 9}
result = 0

for i in reversed(range(3)):
    print(i)
    color = input()
    if i>0 and color in dic:
        result += (10**(i-1))*dic[color] 
    else:
        result *= (10**dic[color])

print(result)

#틀린 내 풀이

'''

color = ['black', 'brown', 'red', 'orange','yellow', 'green','blue','violet','grey','white']
a = color.index(input())
b = color.index(input())
c = color.index(input())
result = int(str(a) + str(b)) * (10**c)
print(result)