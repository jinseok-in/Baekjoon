import math

N = int(input())

count = 0

for B in range(1, 501):
    A_square = B * B + N
    A = int(math.isqrt(A_square))

    if A * A == A_square and B <= A <= 500:
        count += 1

print(count)