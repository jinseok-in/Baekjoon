A, B = map(int, input().split())
C = int(input())
D = B+C
if D >= 60 :
    A = int(A+(D/60))
    if A >= 24 :
        A = A-24
        print(A, D%60)
    else :
        print(A, D%60)
else:
    print(A, D)