n = int(input())

result = []

for i in range(n) :
    ps = input()
    result_append = ""
    vps = []

    for i in range(len(ps)) :
        if ps[i] == "(" :
            vps.append("(")
        elif ps[i] == ")" :
            if len(vps) > 0 :
                vps.pop()
            else :
                result_append = "NO"
                break
        result_append = "YES"
    if len(vps) > 0 :
        result.append("NO")
    else :
        result.append(result_append)

for i in result :
    print(i)