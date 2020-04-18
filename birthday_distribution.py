n=int(input())#Enter number of squares
s=list(map(int,input().split()))
dm=list(map(int,(input().split())))#date and month
i=0
j=0
li=s
for w in range(1,dm[1]+1):
    if li[0]+li[w]==dm[0]:
         j=j+1
         print(li.pop(0))
         print(li.pop(w))
         print("Y")
         print("removed li ",li)
         #print(li[0])
         #print("w=",w)
    #i=i+1
    #if i>len(li):
      #  break
    print("W",w)
    print(li)
    print("interation")
print(j)
