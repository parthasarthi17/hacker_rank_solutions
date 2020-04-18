n=int(input())#Enter number of rows and columns
matrix=[]
for i in range(n):
    x=list(map(int,input().split()))
    matrix.append(x)
sum_1=0
j=0
for i in range(n):
    if(matrix[i][j]==matrix[j][i]):
        sum_1=matrix[i][j]+sum_1
    j=j+1
print(sum_1)#getting sum of diagonals from left to right
sum_2=0
i=0
while i<n:
    sum_2=matrix[i][n-i-1]+matrix[n-i-1][i]+sum_2
    i=i+1
    sum_2=(sum_2)
sum_2=sum_2/2
print(sum_2)
result=sum_1-sum_2
if result<=0:
    result=result*-1
print(result)