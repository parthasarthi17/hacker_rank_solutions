n=list(map(int,input().split()))#Entering n and k
ar=list(map(int,input().split()))#Entering array
i=0
j=1
s=0
print(n[1])
while i<j:
     for w in range(len(ar)-1):
        i=w
        if j==i:
            continue
        elif (ar[i]+ar[j])%n[1]==0:
            s=s+1
     i=i+1
     j=j+1
     if j==len(ar):
        break
print(s)