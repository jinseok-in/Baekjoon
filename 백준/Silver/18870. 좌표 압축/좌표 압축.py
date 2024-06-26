import sys
inputt = sys.stdin.readline

n = int(inputt())
x = list(map(int,inputt().split()))
s_x = sorted(set(x))
arr = {}
for i in range(len(s_x)) :
    arr[s_x[i]] = i
for i in range(len(x)) :
    print(arr[x[i]], end=' ')