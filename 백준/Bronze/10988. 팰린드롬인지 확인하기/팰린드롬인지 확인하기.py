S = str(input())

if len(S)%2==0 :
    a = S[(len(S)//2):]
    if S[:(len(S)//2)] == a[::-1] :
        print(1)
    else :
        print(0)
elif len(S)%2==1 :
    a = S[(len(S)+1)//2:]
    if S[:(len(S)-1)//2] == a[::-1] :
        print(1)
    else :
        print(0)