s=input() # enter string to be repeated
n=eval(input()) # no of time a string is to be repeated
li=s*n
li=list(li)
count=0
for w in range(n):
    if li[w]=='a':
        count+=1
print(count)
