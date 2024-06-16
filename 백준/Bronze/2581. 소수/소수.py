M = int(input())
N = int(input())

t_li = []
if M < N :
    for i in range(M, N+1) :
        cnt = 0
        for j in range(1, i) :
            if i%j==0 :
                cnt += 1
        if cnt == 1:
            t_li.append(i)
    if (len(t_li)==0):
        print(-1)
    else :
        print(sum(t_li))
        print(min(t_li))
elif M>=N :
    if M==1 :
        print(-1)
    else:
        print(M)
        print(M)
