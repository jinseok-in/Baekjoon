n = int(input())

for i in range(1, n + 1):
    l = ' ' * (n - i)
    
    if i == 1:
        print(l + '*')
    else:
        m = ' ' * (2 * i - 3)
        print(l + '*' + m + '*')
