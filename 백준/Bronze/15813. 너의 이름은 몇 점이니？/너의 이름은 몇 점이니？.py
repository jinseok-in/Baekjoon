N = int(input())
name = list(input())
score = 0
for i in range(N) :
    score += ord(name[i])-64
print(score)