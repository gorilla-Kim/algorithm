n = int(input())
rn = input().split()
req = {}
if(len(rn)<=n):
    for i in rn:
        i = int(i)
        if(not i in req):
            req[i] = 0
        req[i] += 1
    for i in range(1,24):
        if(not i in req):
            req[i] = 0
for i in req.values():
    print(i, end=" ")
