n = int(input())

def fibo_bi(n) :
    fibo = [1] * 3
    count = 0
    if n <= 3 :
        return fibo[n-1]
    
    for i in range(3, n+1) :
        fibo.append(fibo[i-1] + fibo[i-3])
    
    return fibo[n-1]

print(fibo_bi(n))