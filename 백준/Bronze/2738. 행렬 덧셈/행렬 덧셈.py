N, M = map(int, input().split())
if (abs(N) <=100) and (abs(M)<=100):
    A = []
    B = []
    C = [A,B]
    for c in C :
        for index in range(N) :
            h = list(map(int, input().split()))
            if len(h) == M :
                c.append(h)

    for i in range(N) :
        for j in range(M) :
            r = (A[i][j] + B[i][j])
            print(r, end=' ')
        print('')

