N, M = map(int,input().split())
c = sorted(list((map(int, input().split()))))
a = 0
for i in c :
    for j in c :
        if i == j :
            continue
        for k in c :
            if (j==k) or (i==k) :
                continue
            elif i+j+k>a :
                if i+j+k <= M:
                    a = i+j+k
print(a)