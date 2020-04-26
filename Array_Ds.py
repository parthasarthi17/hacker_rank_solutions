n=int(input())
a=list(map(int,input().split()))
b=len(a)-1
while b>-1:
    print(a[b],end=' ')
    b-=1