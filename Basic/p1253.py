a,b = input().split()

start = int(a) if int(a)<int(b) else int(b)
for i in range( start, int(a)+1 if start==int(b) else int(b)+1 ):
    print(i, end=" ")