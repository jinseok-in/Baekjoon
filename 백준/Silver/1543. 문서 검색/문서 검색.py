import sys

li = sys.stdin.readline().rstrip()
a = sys.stdin.readline().rstrip()

li_len = len(li)
a_len = len(a)

count = 0
i = 0

while i <= li_len - a_len:
    if li[i : i + a_len] == a:
        count += 1
        i += a_len
    else:
        i += 1

print(count)