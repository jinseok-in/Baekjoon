class person(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "'"+self.name+"'"

def solution(li):
    tmp_dict = {}
    for i in range(len(li)) :
        tmp_dict[person(li[i])] = ''

    return tmp_dict


N = int(input())
a = list(map(str, input().split()))
M = int(input())
b = list(map(str, input().split()))
num_c = {}
int_c = {}
for i in range(len(a)) :
    if a[i] in num_c :
        num_c[a[i]] += 1
    else :
        num_c[a[i]] = 1

int_c = solution(b)
        
for int_key, v in int_c.items() :
    try :
        print(num_c[str(int_key)], end=' ')
    except :
        print(0, end=' ')

