N, M = map(int, input().split())
basket = []

for i in range(N):
    basket.append(i+1)

for ball in range(M) :
    basket_em = []
    i, j = map(int, input().split())
    basket_em.append(basket[i-1])
    basket_em.append(basket[j-1])
    basket[i-1], basket[j-1] = basket_em[1], basket_em[0]
for i in basket :
    print(i, end=" ")