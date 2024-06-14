def solution(board, h, w):
    n = board
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    count = 0
    for i in range(0, 4, 1) :
        h_check = h+dh[i]
        w_check = w+dw[i]
        if (h_check >= 0) and (h_check < len(n)) and (w_check >= 0) and (w_check < len(n)) :
            if board[h][w] == board[h_check][w_check] :
                count += 1
    answer = count
    return answer
board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1
solution(board, h, w)