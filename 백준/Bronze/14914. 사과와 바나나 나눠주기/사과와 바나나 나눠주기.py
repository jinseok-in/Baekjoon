def hand_out(apple, banana) : 
    result = []
    for i in range(1, min(apple, banana) + 1) :
        if apple % i == 0 and banana % i == 0 :
            result.extend([i, apple // i, banana // i])
    return result

apple, banana = map(int, input().split())
result = hand_out(apple, banana)

for i in range(len(result)) :
    if i % 3 == 0 and i != 0 :
        print()
    print(result[i], end = " ")