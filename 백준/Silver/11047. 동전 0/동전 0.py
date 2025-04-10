n, k = map(int, input().split())

won = []
for i in range(n) :
    won.append(int(input()))

result = 0
for i in range(len(won)-1, -1, -1) :
    if won[i] > k :
        continue
    else :
        result += k//won[i]
        k = k % won[i]
print(result)