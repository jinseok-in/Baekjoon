N = int(input())
a = []
for i in range(N) :
    a.append(list(map(int, input().split())))
a = sorted(a, key=lambda x:(x[1], x[0]))
for i in a :
    print(i[0], i[1])