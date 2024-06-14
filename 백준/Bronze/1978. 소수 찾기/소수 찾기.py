N = int(input())
a = list(map(int, input().split()))
t = 0
if len(a) == N :
    for j in a :
        cnt = 0
        for k in range(1, j) :
             if j%k==0 :
                 cnt += 1
        if cnt == 1:
             t += 1
print(t)