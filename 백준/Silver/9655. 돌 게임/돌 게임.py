num = int(input())
li = [False] * (num + 4)

li[1] = True
li[2] = False
li[3] = True

for i in range(4, num + 1):
    li[i] = not li[i - 1] or not li[i - 3]

print("SK" if li[num] else "CY")