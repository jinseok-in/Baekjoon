N = int(input())
TF = True
cnt = 1
a = 1

while TF :
    if a >= N :
        print(cnt)
        TF = False
        break
    a += cnt*6
    cnt += 1