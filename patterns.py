def pattern(x):
    for i in range(x):
       j=x-i-1
       while j>0:
            print(" ",end="")
            j=j-1
       for k in range(0,i+1):
            print("#",end="")
       print()
x=int(input())#Entering heigth of #
pattern(x)