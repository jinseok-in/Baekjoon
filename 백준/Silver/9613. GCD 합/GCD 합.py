def gcd(a,b):
    while b != 0:
       u = a%b
       (a,b) = (b,u)
    return abs(a)

n = int(input())
result = []
count = []

for i in range(n) :
    li = list(map(int, input().split()))
    for j in range(1, len(li)) :
        for k in range(j+1, len(li)) :
            if j == k :
                continue
            count.append(gcd(li[j], li[k]))
             
    result.append(sum(count))
    count = []

for i in result :
    print(i)