from itertools import combinations

def find_winner(N, cards_list):
    max_digit = -1
    winner = -1

    for i in range(N):
        cards = cards_list[i]
        best = 0

        for comb in combinations(cards, 3):
            total = sum(comb)
            last_digit = total % 10
            if last_digit >= best:
                best = last_digit

        if best >= max_digit:
            max_digit = best
            winner = i + 1  # 사람 번호는 1부터 시작
    return winner

if __name__ == "__main__":
    N = int(input())
    cards_list = [list(map(int, input().split())) for _ in range(N)]
    print(find_winner(N, cards_list))