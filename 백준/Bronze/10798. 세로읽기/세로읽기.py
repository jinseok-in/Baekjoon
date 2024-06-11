t_list = []
one_list = []
c = 0
for i in range(5):
    one_list.append(input())
    if (c < len(one_list[0])):
        c = len(one_list[0])
    t_list.append(one_list)
    one_list = []

for c in range(c) :
    for i in range(5) :
        try :
            print(t_list[i][0][c], end='')
        except :
            continue