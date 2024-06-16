x, y, w, h = map(int, input().split())
x_w = x
x_z = x
y_h = y
y_z = y
if x > y :
    r = x
elif x < y :
    r = y
else :
    r = x
for i in range(1,r+1) :
    cnt = i
    if x_w+i==w :
        break
    elif x_z-i==0 :
        break
    elif y_h+i==h :
        break
    elif y_z-i==0 :
        break
print(cnt)