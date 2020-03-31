n = int(input())
arr= []
if(n!=0):
    while(n != 1):
        m = n//2
        j = n%2
        if(j==0):
            arr.append(0)
        else:
            arr.append(1)
        n = m
    arr.append(1)
else:
    arr.append(0)
arr.reverse()
for i in arr:
    print(i, end="")