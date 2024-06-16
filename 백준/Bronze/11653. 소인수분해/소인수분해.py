N = int(input())
so = []
m_so = []
while True :
    if N == 1 :
        break
    else :
        for i in range(2, N) :
            if N%i==0 :
                so.append(i)
        for i in so[::-1] :
            if N%i==N :
                print(N)
                break
            elif N%i==0 :
                print(N//i)
                N = N//(N//i)
            elif N%i==N :
                print(N)
                break
    print(N)
    break