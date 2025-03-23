n = int(input())
nums = set(map(int, input().split()))

print(" ".join(map(str, sorted(nums))))