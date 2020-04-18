def findPairs(lst, K):  
    res = [] 
    while lst: 
        num = lst.pop()
        print(num)
        diff = K - num
        print(diff)
        if diff in lst: 
            b=res.append((diff, num)) 
            print(b)  
    res.reverse() 
    return res 
      
# Driver code 
lst = [1, 5, 3, 7, 9] 
K = 12
print(findPairs(lst, K)) 