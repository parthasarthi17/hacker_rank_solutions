n=int(input())#Enter number of students
b=[]
for i in range(n):
    a=int(input())#Enter marks
    b.append(a)
   # print(b)
x=0

for w in b:
  #  print(w)
    if w <38:
        print(w)
    elif w%5>2 and w>=38 and w<100:
            while 1:
                if x>(w):
                    print(((w//5)*5)+5)
                    break
                x=(x+1)
               # print("x",x)
    else :
            print(w)
