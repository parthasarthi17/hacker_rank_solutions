from collections import Counter
n, arr = input(), Counter(map(int,input().split()))
a=lambda y, x:max(arr[x] + arr[x + 1], y, range(100), -1)
print(a(n,arr))
