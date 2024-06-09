S = str(input()).upper()
A = list(set(S))
S_list = list(S)
c = []
count = 0
r = []
for i in range(len(A)) :
    c.append(S_list.count(A[i]))
for i in range(len(c)) :
    if c[i] == max(c) :
        count += 1
        r.append(A[i])
if count >= 2 :
    print('?')
else :
    print(r[0])