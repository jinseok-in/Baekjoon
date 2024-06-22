N = int(input())
a = []
for i in range(N) :
    a.append(list(map(str, input().split())))
a = sorted(a, key=lambda x:(int(x[0])))
for i in a :
    print(i[0], i[1])