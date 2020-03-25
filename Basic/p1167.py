numList = input().split()
k=0
while(k<len(numList)-1):
    for i in range(len(numList)):
        if(i>0):
            if(int(numList[i])<int(numList[i-1])):
                pre = int(numList[i-1])
                numList[i-1] = int(numList[i])
                numList[i] = pre
    k = k+1
print(numList[1])