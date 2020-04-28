n=int(input())
arr=list(map(int,input().split()))
count_max=0
count_li=[]
for w in arr:
    count_li.append(arr.count(w))
print(len(arr)-max(count_li))
