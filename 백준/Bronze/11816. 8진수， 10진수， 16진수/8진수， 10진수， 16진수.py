n = input()

if str(n).startswith("0x") :
    print(int(n, 16))
elif str(n).startswith("0") :
    print(int(n, 8))
else :
    print(int(n, 10))
