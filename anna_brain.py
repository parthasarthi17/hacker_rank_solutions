n=list(map(int,input().split()))
b=list(map(int,input().split()))
charge=int(input())
sum1=0
for i in b:
    sum1=sum1+i
brain=(sum1-b[n[1]])/2
if brain==charge:
    print("Bon Appetit")
else :
    print(int(charge-brain))