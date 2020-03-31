n = int(input())
arr = input().split()
idx = 0

for i in range(0, n):
    for j in range(0, n):
        if((j+idx)<=(n-1)):
            print(arr[j+idx], end=" ")
        else:
            print(arr[j+idx-n], end=" ")
    print()
    idx += 1