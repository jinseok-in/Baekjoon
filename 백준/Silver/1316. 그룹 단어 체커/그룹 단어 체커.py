N = int(input())
t = 0
for i in range(N) :
    s = str(input())
    s_list = list(s)
    c_list = list(set(s))
    break_for = 0
    for c in c_list :
        if break_for >= 1 :
            break
        check = [0]
        a = ''
        for s in range(len(s_list)) :
            a += str(check[s])
            
            if s_list[s] == c :
                if '10' in a :
                    break_for += 1
                    break
                check.append(1)
            else :
                check.append(0)
    if break_for == 0 :
        t += 1
print(t)