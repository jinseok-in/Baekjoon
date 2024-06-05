N_list = []
for i in range(9) :
    N = int(input())
    N_list.append(N)
print(f'{max(N_list)}\n{N_list.index(max(N_list))+1}')