n,k=map(int,input().split()) #no_of_chapters,no_of_problems_per_page
arr=list(map(int,input().split()))
print(arr)
li=[]
mini=[]
for i in range(len(arr)):
    for m in range(1,k+1):
        mini.append(m)
    li.append(mini)
    mini=[]
print(li)