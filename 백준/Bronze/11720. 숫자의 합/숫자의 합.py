N = str(input())
c = 0
num = str(input())
if len(num)==int(N) :
    for i in range(len(num)) :
        c += int(num[i])
print(c)