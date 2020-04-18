def ratio(a):
    plus=0
    minus=0
    zero=0
    for w in a:
        if w>0:
            plus=plus+1
        elif w<0:
            minus=minus+1
        else :
          zero=zero+1
    plus=plus/len(a)
    minus=minus/len(a)
    zero=zero/len(a)
    return plus,minus,zero
n=int(input())
x=list(map(int,input().split()))
w=ratio(x)
print(w[0])
print(w[1])
print(w[2])
