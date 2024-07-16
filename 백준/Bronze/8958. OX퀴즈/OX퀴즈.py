n = int(input())
for i in range(n) :
    input_data = list(input())
    check = 'b'
    score = 0
    ch_score = 0
    for j in input_data :
        if check == 'b' :
            if j=='O' :
                check = 'O'
                score += 1
                ch_score += 1
            else :
                check = 'X'
        elif j == 'O' :
            if check == 'O' :
                check = 'O'
                score += ch_score + 1
                ch_score += 1
            else :
                check = 'O'
                score += 1
                ch_score = 1
        else :
            check = 'X'
            ch_score = 0
    print(score)