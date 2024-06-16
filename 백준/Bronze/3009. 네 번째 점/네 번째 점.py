f_xy = list(map(int, input().split()))
s_xy = list(map(int, input().split()))
t_xy = list(map(int, input().split()))
xy = []
if (len(f_xy)==2)and(len(s_xy)==2)and(len(t_xy)==2) :
    all_x = [f_xy[0], s_xy[0], t_xy[0]]
    all_y = [f_xy[1], s_xy[1], t_xy[1]]
    setall_x = list(set(all_x))
    setall_y = list(set(all_y))
    for i in setall_x :
        if all_x.count(i) == 1 :
            xy.append(i)
    for i in setall_y :
        if all_y.count(i) == 1 :
            xy.append(i)
    print(xy[0], xy[1])