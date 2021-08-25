# 2021.08.25
# 3029
# 경고

now = list(map(int, input().split(':')))
tar = list(map(int, input().split(':')))
result = []

t_now = now[0]*60*60 + now[1]*60 + now[2]
t_tar = tar[0]*60*60 + tar[1]*60 + tar[2]
if t_tar > t_now:
    t_result = t_tar - t_now
else:
    t_result = t_tar+24*60*60 - t_now

result.append(t_result//3600)
result.append(t_result % 3600//60)
result.append(t_result % 60)

print("{:02d}:{:02d}:{:02d}".format(result[0], result[1], result[2]))
