n = int(input())

result_s = []
result_m = []
for j in range(n) :
    li = list(map(int, input().split()))

    li_num = []

    for i in li :
        if i % 2 == 0 :
            li_num.append(i)
    result_s.append(sum(li_num))
    result_m.append(min(li_num))

for i in range(n) :
    print(result_s[i], result_m[i])
