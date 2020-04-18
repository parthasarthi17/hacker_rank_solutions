def sum(ar):
    a=0
    for w in ar:
        a=a+w
    return a


if __name__=='__main__':
    a=int(input()) # Entering size of array
    i=0
    while 1:
        if a>=0:
            break
        else :
            a=int(input()) # Enter size greater than equal to zero
        
    b=[]
    i=0
    while i<a:
        c=int(input())#inputing numbers
        b.append(c)
        i=i+1
    print(sum(b))
    