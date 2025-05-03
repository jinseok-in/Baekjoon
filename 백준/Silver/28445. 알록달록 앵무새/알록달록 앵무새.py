w = input()
w += " " + input()

all_li = w.split()

set_li = sorted(list(set(all_li)))

for i in set_li :
    for j in set_li :
        print(i, j)