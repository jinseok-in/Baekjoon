def count(dic):
    count_num = 1
    for items in dic.values():
        count_num *= (len(items) + 1)
    return count_num - 1

result = []
num = int(input())

for _ in range(num) :
    n_t = int(input())
    dic = {}
    for i in range(n_t) :
        clothes, c_type = input().split()
        if c_type in dic :
            dic[c_type].append(clothes)
        else :
            dic[c_type] = [clothes]
    result.append(count(dic))

for i in result :
    print(i)