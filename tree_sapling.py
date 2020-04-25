t=int(input()) # no_of_test_cases
li=[]
for i in range(t):
    n=int(input())
    li.append(n)
#li=[0,1,4]
height=1
for j in range(len(li)):
    for w in range(li[j]):
        if w%2==1:
            height=height+1
        else :
            height*=2
    print(height)
    height=1    
