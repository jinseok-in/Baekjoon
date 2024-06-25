N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
num_c = {}
int_c = {}
for i in range(len(a)) :
    num_c[a[i]] = ''
for i in range(len(b)) :
    int_c[b[i]] = ''
for int_key in int_c :
    if int_key in num_c :
        print(1, end=' ')
    else :
        print(0, end=' ')