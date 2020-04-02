a=[]
for i in range(20):
    a.append([]) 
    for j in range(20): 
        a[i].append(0) 
for i in range(19): 
    b=input().split() 
    for j in range(19): 
        a[i+1][j+1]=int(b[j]) 
c=int(input()) 
for i in range(c):
    d,e=map(int,input().split()) 
    for j in range(1,20):
        if a[j][e]==0: 
            a[j][e]=1
        else:a[j][e]=0 
        if  a[d][j]==0: 
            a[d][j]=1
        else:a[d][j]=0 
for i in range(1,20): 
    for j in range(1,20): 
        print(a[i][j],end=' ') 
    print() 