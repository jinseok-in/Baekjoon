n = int(input())
a = {}
b = []
for i in range(n) :
    nm, el = map(str, input().split())
    a[nm] = el
for key, value in sorted(a.items(), reverse=True) :
    if value == 'enter' :
        print(key)
