def fact(n):
    if n==1:
        print("yhn")
        return 1
        
    else :
        return n*fact(n-1)
n=int(input())
print(fact(n))