n, m = map(int, input().split())
a = {}
b = {}
cnt = 0
for i in range(n) :
    a_k = str(input())
    if a_k in a :
        a[a_k] += 1
    else :
        a[a_k] = 1

for i in range(m) :
    b_k = str(input())
    if b_k in b :
        b[b_k] += 1
    else :
        b[b_k] = 1
val = 0
for key, values in b.items() :
    if key in a :
         val += values
print(val)