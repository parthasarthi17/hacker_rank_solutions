n=int(input())#no_of_days
shared=5//2
liked=2
sum1=2
for w in range(n-1):
    shared=liked*3
    liked=shared//2
    sum1=sum1+liked
print(sum1)