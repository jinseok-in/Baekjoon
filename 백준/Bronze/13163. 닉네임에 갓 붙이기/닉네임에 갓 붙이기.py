n = int(input()) 
nick_name = []
for i in range(n) :
    nick_name.append(list(input().split())[1:])

for i in range(n) :
    print("god", end="")
    print("".join(nick_name[i]))