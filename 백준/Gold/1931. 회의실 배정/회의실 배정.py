a = int(input())
b = []
for i in range(a) :
    q, w = map(int, input().split(" "))
    b.append((q, w))

b.sort(key = lambda x : (x[1], x[0]))
count = 0
c = 0

for x_f, x_s in b :
    if c <= x_f :
        count += 1
        c = x_s

print(count)