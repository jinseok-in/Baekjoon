n = int(input())

# 윗줄: 5칸 전부 '@'
for _ in range(n):
    print('@' * (5 * n))

# 중간 줄: 왼쪽 1칸만 '@'
for _ in range(3 * n):
    print('@' * n)

# 아랫줄: 다시 5칸 전부 '@'
for _ in range(n):
    print('@' * (5 * n))
