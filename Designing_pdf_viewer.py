#n=[ 1,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
n=list(map(int,input().split()))
word=input()
s=len(word)
word=list(word)
#print(word)
i=0
li=[]
for w in word:
    x=ord(w)-97
    li.append(n[x])
#print(li)
max_height_word=0
for j in li:
    if j>max_height_word:
        max_height_word=j
print(max_height_word*(len(li)))
