first = list(map(int,input().split()))
second = list(map(int,input().split()))
second.sort()
for i in range(0, first[0] if first[0]!=0 else 1):
    print("{0} ".format(second[i]), end="" if (i+1)%first[1] else "\n")
