def count(li):
    maxcount,maxvalue=0,0
    for i in li:
        count=0
        for j in range(len(li)):
            if li[j]==li[i]:
                count=count+1
        if count>maxcount:
            maxcount=count
            maxvalue=li[i]
    return maxvalue

n=int(input())
li=list(map(int,input().split()))
print(count(li))

