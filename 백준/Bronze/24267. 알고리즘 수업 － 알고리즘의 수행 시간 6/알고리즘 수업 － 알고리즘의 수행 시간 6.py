N = int(input())
cha = 0
for i in range(1,4) :
    cha+=i
cnt = (N)*(N-1)*(N-2)//cha

print(cnt)
print(3)