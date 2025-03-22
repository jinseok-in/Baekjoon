import sys

li = [0] * 10001
li[0] = 1

for a in [1, 2, 3] :
    for b in range(a, 10001) :
        li[b] += li[b - a]

num = int(sys.stdin.readline().strip())

for i in range(num) :
    a = int(sys.stdin.readline().strip())
    print(li[a])