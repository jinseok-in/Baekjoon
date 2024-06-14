N, K = map(int, input().split())
A = []
if N == K :
    print(1)
else :
    for i in range(1,N+1) :
        if N%i == 0 :
            A.append(i)
    if len(A) >= K :
        print(A[K-1])
    else :
        print(0)