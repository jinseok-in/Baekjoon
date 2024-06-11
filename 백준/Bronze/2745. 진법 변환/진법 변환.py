N, B = map(str, input().split())
N = list(N)
result = []
a = []
b = []
c = []
r = []

for i in range(10) :
    a.append(str(i))
for i in range(26) :
    b.append(chr(i+65))
for i in range(36) :
    c.append(str(i))

for i in range(len(N)) :
    if N[i] in a :
        r.append(str(a[a.index(N[i])]))

    elif N[i] in b :
        r.append(c[b.index(N[i])+10])

sum = 0

for i in range(len(r)) :
    sum += (int(B)**(len(r)-i-1))*int(r[i])
print(sum)