S = str(input())
alpha = []
S_sli = []
a_list = []
for i in range(26):
    alpha.append(chr(i+97)) 
for i in range(len(S)):
    S_sli.append(S[i])

for i in alpha :
    if i in S_sli :
        print(S_sli.index(i), end=' ')
    else :
        print(-1, end=' ')