import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
result = []

for _ in range(n):
    cmd = input().strip()
    
    if cmd.startswith("push"):
        _, num = cmd.split()
        queue.append(int(num))
    elif cmd == "pop":
        result.append(str(queue.popleft() if queue else -1))
    elif cmd == "size":
        result.append(str(len(queue)))
    elif cmd == "empty":
        result.append("1" if not queue else "0")
    elif cmd == "front":
        result.append(str(queue[0] if queue else -1))
    elif cmd == "back":
        result.append(str(queue[-1] if queue else -1))

print('\n'.join(result))