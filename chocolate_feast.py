T = int(input())
    
for _ in range(T):
        N, C, M = map(int,input().split())
        
        total = N // C
        wrappers = total
        
        while wrappers >= M:
            wrappers += 1 - M
            total += 1
        
        print(total)