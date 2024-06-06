N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(i+1)

for trans in range(M):
    i, j = map(int, input().split())
    A = basket[i-1:j][::-1]
    del basket[i-1:j]
    for insert in range(i-1, j) :
        basket.insert(insert, A[0])
        A.pop(0)
for result in basket :
    print(result, end=" ")