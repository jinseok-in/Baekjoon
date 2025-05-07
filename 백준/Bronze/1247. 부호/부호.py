result = []
for _ in range(3) :
    a = 0
    for i in range(int(input())) :
        a += int(input())
    if a == 0 :
        result.append("0")
    elif a > 0 :
        result.append("+")
    elif a < 0 :
        result.append("-")

for i in result :
    print(i)