def Euclidean(a, b) :
    while b != 0 :
        [a, b] = [b, a%b]
    return a


a_1, a_2 = map(int, input().split())
b_1, b_2 = map(int, input().split())
if a_2 != b_2 :
    re1 = (a_1*b_2) + (a_2*b_1)
    re2 = a_2*b_2
else :
    re1 = a_1+b_1
    re2 = a_2
    
eu = Euclidean(re1, re2)
if eu > 1 :
    print(re1//eu, re2//eu)
else :
    print(re1, re2)