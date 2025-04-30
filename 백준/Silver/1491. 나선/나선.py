import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())

    if N <= 0 or M <= 0:
        print(0, 0)
        return

    visited = [[False for _ in range(M)] for _ in range(N)]

    x, y = 0, 0
    visited[x][y] = True
    count = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_idx = 0

    while count < N * M:
        next_x = x + dx[dir_idx]
        next_y = y + dy[dir_idx]

        if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
            x, y = next_x, next_y
            visited[x][y] = True
            count += 1
        else:
            dir_idx = (dir_idx + 1) % 4
            next_x = x + dx[dir_idx]
            next_y = y + dy[dir_idx]

            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                x, y = next_x, next_y
                visited[x][y] = True
                count += 1
            else:
                break

    print(x, y)

solve()