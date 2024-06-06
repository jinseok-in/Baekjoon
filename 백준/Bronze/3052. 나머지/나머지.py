num = []
for i in range(10):
    num.append(int(input()))

for i in range(len(num)) :
    num[i] = num[i]%42

count = set(num)
print(len(count))