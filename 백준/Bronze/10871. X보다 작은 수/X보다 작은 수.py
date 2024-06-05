N, X = map(int, input().split())
A = list(map(int, input().split()))
row = []
if len(A) == N :
    for i in A :
        if i < X :
            row.append(i)
        else:
            continue
for i in row :
    print(f'{i}', end=" ")