n,q=map(int,input().split())
li=[]
for i in range(q):
    b=list(map(int,input().split()))
    li.append(b)
last_answer=0
seq=[]
i,j=0,0
while j<3:
    while i<3:
        if li[j][i]==1:
            (li[j][i]^last_answer)%n
            seq.append(li[j][2])
            print(seq)

        elif li[j][i]==2:
            print("Yhn")
        i+=1
    j+=1
    i=0