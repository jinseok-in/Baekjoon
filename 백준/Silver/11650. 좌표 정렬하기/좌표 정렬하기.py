N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
a = sorted(a, key=lambda x : (x[0], x[1]))
for i in range(len(a)) :
    print(a[i][0], a[i][1])