import sys
for i in range(100):
    try :
        a = input()
        if a == '' :
            break
        else:
            print(a)
    except EOFError :
        break