t=int(input()) #no of test cases
li=[]
for w in range(t):
    n,c,m=list(map(int,input().split()))#total money ,cost of chocolate,no of wrappers returned for 1 chocolate
    k=n,c,m
    li.append(k)
print(li)
noc=n//c #no of chocolate
now=noc #no of wrappers
wl=now%m #wrapper_left
print(wl)
noc+=now//m
wl+=now//m
noc+=now//m
wl+=now//m
print(wl)
print(noc)

