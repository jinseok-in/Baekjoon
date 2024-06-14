import math
A, B, V = map(int, input().split())
m = A
day = 0
day = math.ceil((V-B)/(A-B))
print(day)