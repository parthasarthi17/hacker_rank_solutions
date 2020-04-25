player=int(input())
leadership=list(map(int,input().split()))
no_of_games=int(input())
scores=list(map(int,input().split()))
li=[]
i=0
rank=1
for w in range(player-1):
    if leadership[i]==leadership[i+1]:
        b=rank,leadership[i]
        i=i+1
        rank=rank-1
    else:
        b=rank,leadership[i]
        i+=1
    li.append(b)
    rank+=1
if leadership[player-2]==leadership[player-1]:
    b=rank-1,leadership[player-1]
    li.append(b)
else:
    b=rank,leadership[player-1]
    li.append(b)
print(li)#determining ranks
rank_of_alice=player-1
sum1=int(scores[0])
i=0
for w in leadership:
    if sum1>=int(li[player-1][1]):
        rank_of_alice-=1
    sum1=sum1+scores[i]
    b=i
    for x in range (0,len(leadership)-1):
        #print("..")
        if sum1>int(li[player-1][1]):
           #rank_of_alice -= 1
           i=i
        elif(x>=1) and b!=len(scores):
               i=i+1
               print("..2")
               #rank_of_alice-=1
        sum1=sum1+scores[i]
        b=0
               
    print(rank_of_alice)
