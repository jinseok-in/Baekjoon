a = []
b = []
c = []
count = 2
[a.append(chr(i+65)) for i in range(26)]
for i in range(8) :
    if (i == 5) or (i == 7) :
        for j in range(4) :
            b.append(count)
    else :
        for j in range(3) :
            b.append(count)
    count += 1
S = str(input())
for i in range(len(S)) :
    c.append(int(b[a.index(S[i])])+1)
print(sum(c))