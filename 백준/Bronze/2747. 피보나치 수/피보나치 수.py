a = []
for i in range(46):
    if (i==0) or (i==1):
        a.append(i)
    else :
        a.append(a[i-2] + a[i-1])
num = int(input())
print(a[num])