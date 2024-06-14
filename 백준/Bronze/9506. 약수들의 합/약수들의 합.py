bre = 0
while bre == 0 :
    arr = []
    total = 0
    N = int(input())
    if N == -1 :
        bre =1
        break
    elif N == 0 :
        print('0 = 0')
        continue
    for i in range(1, N+1) :
        if N%i == 0:
            arr.append(i)
    total = sum(arr[:-1])
    #for i in arr[:-1] :
    #    total += i
    if N == total :
        print(N, '= ',end='')
        print(arr[0], end='')
        for j in range(1, len(arr)-1):
            if j == len(arr)-2 :
                print(' +', arr[j])
            else :
                print(' +', arr[j], end='')
    else :
        print(N, 'is NOT perfect.')