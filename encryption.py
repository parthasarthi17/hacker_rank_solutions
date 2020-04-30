from math import sqrt, floor, ceil
s = input()
n = len(s)
r = int(floor(sqrt(n)))
c = int(ceil(sqrt(n)))
if r * c < n:
    r += 1

res = [[0 for w in range(c)] for k in range(r)]

it = 0
i = 0
j = 0

while it < n:
    res[i][j] = s[it]
    it += 1
    j += 1
    if j == c:
        j = 0
        i += 1
out = ""
print(res)
for i in range(c):
    for j in range(r):
        if res[j][i] != 0:
            out += res[j][i]
    out += " "
print(out)