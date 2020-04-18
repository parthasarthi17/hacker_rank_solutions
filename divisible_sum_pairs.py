from itertools import combinations
def findPairs(lst, n):    
    res = []
    for var in combinations(lst,2): 
        if (var[0] + var[1])%n == 0: 
            res.append((var[0], var[1])) 
        
    return res 
n=list(map(int,input().split())) #n,k
lst=list(map(int,input().split()))
print(len(findPairs(lst,n[1]))) 