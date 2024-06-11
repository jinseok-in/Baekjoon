b_li =[]

n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    for ten in range(b, b+10) :
        ten10 = []
        ten10.append(ten)
        for one in range(a, a+10) :
            one10 = []
            one10.append(one)
            if (one10+ten10) not in b_li :
                b_li.append(one10+ten10)

print(len(b_li))