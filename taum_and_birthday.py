t=int(input()) #no of test cases
li=[]
for w in range(t):
    b,w=map(int,input().split())
    bc,wc,z=map(int,input().split())
    k=[b,w,bc,wc,z]
    li.append(k)
#print(li)
for m in range(len(li)): 
        cost=li[m][2]*li[m][0]+li[m][1]*li[m][3]
        if cost>li[m][2]*(li[m][0]+li[m][1])+li[m][4]*(li[m][1]):
            cost=li[m][2]*(li[m][0]+li[m][1])+li[m][4]*(li[m][1])
        elif cost>li[m][3]*(li[m][0]+li[m][1])+li[m][4]*li[m][0]:
            cost=li[m][3]*(li[m][0]+li[m][1])+li[m][4]*li[m][0]
        print(cost)
