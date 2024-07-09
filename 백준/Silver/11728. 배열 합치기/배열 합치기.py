a, b = map(int, input().split())
word1 = list(map(int, input().split()))
word2 = list(map(int, input().split()))
if len(word1) == a :
    if len(word2) == b :
        word = sorted(word1 + word2)
        for i in word :
            print(i,end=" ")