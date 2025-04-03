result = []
n = int(input())
for i in range(n) :
    re = int(input())
    num_li = list(str(re))
    asc = int(''.join(sorted(num_li)))
    desc = int(''.join(sorted(num_li, reverse=True)))
    count = 0

    while re != 6174 :
        re = desc - asc
        asc = int(''.join(sorted(str(re).zfill(4))))
        desc = int(''.join(sorted(str(re).zfill(4), reverse=True)))
        count += 1
    
    result.append(count)

for i in result :
    print(i)