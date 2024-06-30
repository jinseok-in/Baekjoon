from math import gcd

n = int(input())
a = []
f = int(input())
for i in range(n-1):
    num = int(input())
    a.append(num-f)
    f = num

ro = a[0]
for i in range(1, len(a)):
    ro = gcd(ro, a[i])

cnt = 0
for i in a:
    cnt += i//ro - 1
print(cnt)