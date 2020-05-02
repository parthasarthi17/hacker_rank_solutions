n,m = map(int,input().split())
#n,m = [int(n),int(m)]
c = sorted(map(int,input().strip().split()))
print(c)
j = 0
ans = 0
for i in range(n):
    while j + 1 < len(c) and abs(c[j] - i) > abs(c[j+1] - i):
        j += 1
    ans = max(ans, abs(c[j]-i))

print (ans)