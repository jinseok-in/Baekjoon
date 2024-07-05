a = int(input())
b = int(input())
c = int(input())

g = a*b*c
g_li = list(str(g))
for i in range(10) :
    print(g_li.count(str(i)))