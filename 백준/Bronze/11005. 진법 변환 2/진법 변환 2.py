N, B = map(int, input().split())

N10 = N

r = []
a = []
b = []
result = ''
for i in range(26) :
    a.append(chr(i+65))
for i in range(10, 36) :
    b.append(str(i))

TF = True
while TF :
    r.append(N%B)
    N = N//B
    if N < B :
        r.append(N)
        TF = False
if B == 10:
    print(N10)
else :
    for i in range(len(r)-1, -1, -1) :
        if str(r[i]) in b :
            result = str(a[b.index(str(r[i]))])
            if i == len(r)-1:
                if result == '0' :
                    continue
            print(result, end='')
        else :
            result = str(r[i])
            if i == len(r)-1:
                if result == '0' :
                    continue
            print(result, end='')
