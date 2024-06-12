N = int(input())
for i in range(N) :
    re_dal = int(input())

    q = re_dal//25
    re_dal = re_dal-25*(re_dal//25)
    d = re_dal//10
    re_dal = re_dal-10*(re_dal//10)
    n = re_dal//5
    re_dal = re_dal-5*(re_dal//5)
    p = re_dal//1
    re_dal = re_dal-1*(re_dal//1)

    print(f'{q} {d} {n} {p}')