def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a

def lcm(a, b):
    return (a*b)//Euclidean(a, b)
a,b = map(int,input().split())
print(lcm(a,b))