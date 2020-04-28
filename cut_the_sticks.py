n=int(input())
arr=list(map(int,input().split()))
x=min(arr)
print(len(arr))
li=[]
for w in arr:
    if w>x:
        li.append(w)
w=0
while w<len(li):
    li[w]-=x
    w+=1
li1=[]
print(len(li))

for w in li:
    x=min(li)
    if w>x:
      li1.append(w)

w=0
while w<len(li1):
    li1[w]-=x
    w+=1
print(len(li1))

li2=[]
for w in li1:
    x=min(li1)
    if w>x:
      li2.append(w)

w=0
while w<len(li2):
    li2[w]-=x
    w+=1
print(len(li2))
