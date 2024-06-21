N = int(input())
t = []
for i in range(1,N) :
    N_list = list(str(i))
    s = 0
    sum_n = i
    for j in N_list :
        sum_n += int(j)
        s += int(j)
    if (i+s) == N :
        s = N - int(s)
        t.append(s)
if len(t) == 0 :
    print(0)
else :
    print(min(t))
    
