n, k = input().split()
# 세로열
print("n = {0}, k = {1}".format(n, k))
special = 1
for i in range(1, int(n)+1):
    # 가로열
    if(i==1 or i==int(n)):
        print("*"*int(n))
    else:
        for j in range(1, int(n)+1):
            print("*" if (j+special)%int(k)==0 or j==1 or j==int(n) else " ", end="")
        special += 1
        print()