n=int(input()) #entering size
li=[]
for w in range(n):
    b=input()
    li.append(b)
nq=int(input())#Size of queries
q=[]
for w in range(nq):
    b=input()
    q.append(b)
count=0
licount=[]
i=0
for w in q:
   while i<len(li):
       if w==li[i]:
           count+=1
       i+=1
   print(count)
   count=0
   i=0