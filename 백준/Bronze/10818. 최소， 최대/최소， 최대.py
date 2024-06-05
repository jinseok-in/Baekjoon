N = int(input())
A = list(map(int, input().split()))
if len(A) >= N :
    print(f'{min(A)} {max(A)}')