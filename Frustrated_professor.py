t=int(input()) #Number of test cases
#n,k=list(map(int,input().split())) # n is number of students and k is threshold frequency
#a=list(map(int,input().split())) #arrival time of student
li=[]
for g in range(int(t)):
        count=0
        n,k=list(map(int,input().split())) # n is number of students and k is threshold frequency
        a=list(map(int,input().split()))
        for w in a:
            if w>0:
                count+=1
        if count<k:
            print("Yes")
        else :
            print("No")
        count=0
for c in range(len(li)):
    if li[c]==1:
        print("Yes")
    elif li[c]==0:
        print("No")
    