a, b, c = map(int,input().split())
m = c-b
if m == 0 :
    print(-1)
else :
    r = a//m+1
    if r<=0 :
        r = -1
    print(r)