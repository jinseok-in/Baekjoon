def gcd(a, b) :
    while b != 0 :
        u = a % b
        (a, b) = (b, u)
    return abs(a)

n = int(input())

all_case = []
result = []
for i in range(n) :
    li = list(map(int, input().split()))
    for j in range(len(li)) :
        for k in range(j+1, len(li)) :
            if j == k :
                continue
            all_case.append(gcd(li[j], li[k]))
    result.append(max(all_case))
    all_case = []

for i in result :
    print(i)