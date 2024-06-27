s = input()
cnt = 1
a = set()
while cnt <= len(s)+1 :
    for i in range(cnt, len(s)+1) :
        a.add(s[i-cnt:i])
    cnt += 1
print(len(a))