p = []
m = []
m_num, h, c = 0, 0, 0
a= 0
for i in range(9) :
    p.append(list(map(int, input().split())))
    m.append(max(p[i]))

m_num = max(m)
    
for i in range(9) :
    for j in range(9) :
        if p[i][j] == m_num :
            h = i
            c = j
            if a == 1 :
                break
            a += 1

print(m_num)
print(h+1, c+1)
        