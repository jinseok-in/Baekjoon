bre = 0
while bre == 0 :
    A, B = map(int, input().split())
    if (A == 0) and (B == 0) :
        bre = 1
    elif B%A == 0 :
        print('factor')
    elif A%B == 0 :
        print('multiple')
    else :
        print('neither')