n,d=map(int,input().split()) #no_of_integers,no_of_rotations
arr=list(map(int,input().split()))
front=0
rear=len(arr)-1
anor=d%n#actual_no_of_rotations
temp=[]
for i in range(anor):
    temp.append(arr[i])
#print(temp)
i=0
while i<len(arr)-len(temp):
    arr[i]=arr[len(temp)+i]
    i+=1
j=0
while i<len(arr):
    arr[i]=temp[j]
    i+=1
    j+=1
print(arr)