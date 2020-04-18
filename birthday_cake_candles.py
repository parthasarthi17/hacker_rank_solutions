def birthday_cake_candles(a):
    w=max(a)
    i=0
    for x in a:
        if x==w:
            i=i+1
    return i
n=int(input())#enter no of candles
x=list(map(int,input().split()))
print(birthday_cake_candles(x))