def sum_max_min(a):
    max_sum=0
    min_sum=0
    for w in a:
        max_sum=max_sum+w
    f=max_sum
    max_sum=max_sum-min(a)
    min_sum=f-max(a)
    print(min_sum,max_sum)
x=list(map(int,input().split()))
sum_max_min(x)