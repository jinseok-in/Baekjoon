def goodWord(word):
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    if goodWord(word):
        count += 1

print(count)
