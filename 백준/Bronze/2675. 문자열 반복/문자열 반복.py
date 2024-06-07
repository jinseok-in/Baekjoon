R = int(input())
for i in range(R) :
    c = ''
    a, b = map(str, input().split())
    for k in range(len(b)) :
        c += b[k]*int(a)
    print(c)