a = list(map(int, input()))

set_a = list(set(a))

count = [0]
count_69 = [0]
for i in range(0, len(set_a)) :
    if set_a[i] != 6 and set_a[i] != 9 :
        count.append(a.count(set_a[i]))
    else :
        count_69.append(a.count(set_a[i]))

print(max([max(count), (sum(count_69)+1)//2]))