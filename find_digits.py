t=int(input()) #no_of_test_cases
li=[]
for w in range(t):
    b=int(input())
    li.append(b)
d=[]
i=0
while i <t:
        
        n=li[i]
        count=0
        while n>0:
            Remainder=n%10
            n=n//10
            if Remainder==0:
                  continue
            if li[i]%Remainder==0:
                count+=1
        print(count)
        count=0
        i+=1
