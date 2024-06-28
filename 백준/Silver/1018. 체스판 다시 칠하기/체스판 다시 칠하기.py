import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a_li = [input().strip() for _ in range(n)]

# 체스판의 두 가지 패턴
check_b = ['BWBWBWBW', 'WBWBWBWB'] * 4
check_w = ['WBWBWBWB', 'BWBWBWBW'] * 4

min_changes = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        check_num1 = 0
        check_num2 = 0
        for k in range(8):
            for l in range(8):
                if a_li[i + k][j + l] != check_b[k][l]:
                    check_num1 += 1
                if a_li[i + k][j + l] != check_w[k][l]:
                    check_num2 += 1
        min_changes = min(min_changes, check_num1, check_num2)

print(min_changes)