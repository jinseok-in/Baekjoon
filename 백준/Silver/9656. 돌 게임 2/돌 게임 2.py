num = int(input())
count = 0
while (num > 1) :
    if num > 3 :
        num -= 3
    elif num > 1 :
        num -= 1
    count += 1
if count % 2 == 1 :
    print("SK")
else :
    print("CY")