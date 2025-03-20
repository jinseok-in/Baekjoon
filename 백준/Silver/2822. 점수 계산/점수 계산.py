scores = [(int(input()), i + 1) for i in range(8)]

scores.sort(reverse=True, key=lambda x: x[0])

top_scores = scores[:5]

total_score = sum(score[0] for score in top_scores)

problems = sorted(score[1] for score in top_scores)

print(total_score)
print(' '.join(map(str, problems)))