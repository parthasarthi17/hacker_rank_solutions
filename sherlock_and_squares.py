t=int(input()) #no_of_test_cases
li=[]
for w in range(t):
    a,b=map(int,input().split())
    k=[a,b]
    li.append(k)
count=0
i=0
j=0
k=0
print(li)
while j<t:
        a=li[j][i]+k
        while a<=li[j][1]:
                #print(j,i,a)
                sqrt=a**0.5
                sqrt1=int(sqrt)
                if sqrt==sqrt1:
                    count+=1
                
                i+=1
                k+=1
                a+=1
        j+=1
        i=0
        print(count)
        count=0
        #print("Yhn")