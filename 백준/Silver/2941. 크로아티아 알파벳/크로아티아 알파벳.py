cs = str(input())
cs_len = len(cs)
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_count = []
for i in range(len(croatia)) :
    if croatia[i] in cs :
        croatia_count.append(cs.count(croatia[i]))
print(cs_len-sum(croatia_count))