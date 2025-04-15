q, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
while q < 200 and count < n :
    q += a[count]
    count += 1
print(count)