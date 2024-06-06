N = int(input())
new_score = []

score = list(map(int, input().split()))

for i in range(N):
    new_score.append((score[i]/max(score)*100))
average = sum(new_score)/N
print(average)