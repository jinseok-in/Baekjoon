n = int(input())

result = []
for i in range(n) :
    a, b = map(int, input().split())
    if (b/a) >= 2 and b % a == 0 :
        result.append("1")
    else :
        result.append("0")

for i in result :
    print(i)