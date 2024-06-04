N = int(input())
N_list = list(map(int, input().split()))
if N == len(N_list) :
    v = int(input())
    print(N_list.count(v))