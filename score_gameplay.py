n=int(input())#Enter number of games
score=list(map(int,input().split()))
min_score=score[0]
max_score=score[0]
#print(max_score,min_score)
i=0#max_score_change
j=0#min_score_change
for w in score:
    if w>max_score:
        max_score=w
        i=i+1
    elif w<min_score:
        min_score=w
        j=j+1
print(i,j)