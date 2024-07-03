a = list(input())
b = []
for i in a :
    if i.isupper() :
        b.append(i.lower())
    elif i.islower() :
        b.append(i.upper())
for i in b :
    print(i, end='')