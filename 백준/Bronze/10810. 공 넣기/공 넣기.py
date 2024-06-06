S = input().split()
N, M = int(S[0]), int(S[1])
basket =[]
for i in range(N):
    basket.append(0)
for ball in range(M) :
    method = input().split()
    for insert in range(int(method[0]), int(method[1])+1):
        basket[insert-1] = int(method[2])
for i in basket :
    print(i, end=" ")
