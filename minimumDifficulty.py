number = int(input())

l = list(map(int,input().split(" ")))
p = set()
aMax = l[1]-l[0]
iMax = 0
for x in range(number-1):
    cMax = l[x+1]-l[x]
    if cMax > aMax:
        aMax = cMax
        iMax = x
    p.add(l[x+1]-l[x])
if len(p) != 1: 
    p.remove(aMax)
    sMax = max(p)
else:
    sMax = aMax
q = set()
for t in range(number-2):
    if t != iMax:
        q.add(max((l[t+2] - l[t]),aMax))
    else:
        q.add(max((l[t+2] - l[t]),sMax))


print(min(q))
#len of p will be n-2

