n = int(input())
t = []
tx = []
ty = []
for i in range(n) :
    t.append(list(map(int,input().split())))
for i in t :
    tx.append(i[0])
    ty.append(i[1])
x = max(tx)-min(tx)
y = max(ty)-min(ty)
print(x*y)