def reversedic(dic) :
    return dict(map(reversed, dic.items()))

n, m = map(int,input().split())
dic = {}

for i in range(1, n+1) :
    poke = str(input())
    dic[poke] = str(i)
merge_dic = dic | reversedic(dic) 

for i in range(m) :
    inp = str(input())
    print(merge_dic[inp])