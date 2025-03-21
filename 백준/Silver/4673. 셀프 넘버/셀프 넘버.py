total_list = set([i for i in range(1, 10001)])
num = 1
while (num <= 10000) :
    c = num
    for i in str(num) :
        c += int(i)
    if c in total_list :
        total_list.remove(c)
    
    num += 1
for i in total_list :
    print(i)