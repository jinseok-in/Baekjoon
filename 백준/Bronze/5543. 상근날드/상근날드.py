ham = []
for _ in range(3) :
    ham.append(int(input()))
ham.sort()

drinks = []
for _ in range(2) :
    drinks.append(int(input()))
drinks.sort()

print(ham[0] + drinks[0] - 50)