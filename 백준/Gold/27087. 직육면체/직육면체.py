t = int(input())
for _ in range(t) :
    a, b, c, p = map(int,input().split())
    ch = 0
    if (a >= p) and (a % p == 0) :
        ch += 1
    if (b >= p) and (b % p == 0) :
        ch += 1
    if (c >= p) and (c % p == 0) :
        ch += 1
    if ch >= 2 :
        print(1)
    else :
        print(0)