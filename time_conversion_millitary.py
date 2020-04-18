
s=input()

li=list(s.split(":"))
if (li[2][2]=='P'):
    l=li[0]
    m=li[1]
    n=li[2][0]
    p=li[2][1]
    l=int(l)
    m=int(m)
    n=int(n)
    p=int(p)
    if l<12 and m<60 and n<6 and p<=9:

        a=int(li[0])
        a=a+12
        li[0]=a
      #  print(li)
        str1=str(a)
        i=1
        while i<len(li):
                    str1=str1+":"+li[i]
                    i=i+1
                
        print(str1[:-2])
    elif l==12:
        
        a=int(li[0])
        a="12"
        #li[0]=a
      #  print(li)
        str1=a
        i=1
        while i<len(li):
                    str1=str1+":"+li[i]
                    i=i+1
        print(str1[:-2])
    else :
       s=input() #Enter your time agian
elif(li[2][2]=='A') :
        l=li[0]
        l=int(l)
        if l==12:
            a=int(li[0])
            a="00"
            str1=a
            i=1
            while i<len(li):
                    str1=str1+":"+li[i]
                    i=i+1
            print(str1[:-2])
        else:
            print(s[:-2])
else :
    s=input()