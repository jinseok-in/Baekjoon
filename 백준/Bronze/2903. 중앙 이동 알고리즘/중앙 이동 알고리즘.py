N = int(input())
a2 = 4
for i in range(N) :
    a = int(a2**(1/2))*2-1
    a2 = a**2
print(a2)