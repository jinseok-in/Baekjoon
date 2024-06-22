N = int(input())
a = []
for i in range(N) :
    a.append(str(input()))
a = sorted(list(set(a)), key=lambda x: (len(x), x))
for i in a :
    print(i)