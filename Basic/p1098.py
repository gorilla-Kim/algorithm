size = list(map(int,input().split()))
result = []
# 결과 0으로 초기화
for i in range(size[0]):
    result.append([])
    for j in range(size[1]):
        result[i].append(0)

n = int(input()) # 막대의 개수
arr = [] # 막대정보(size, dir, x, y)
for i in range(n):
    arr.append(list(map(int,input().split())))


for i in arr:
    if(i[1]==0):
        for j in range(i[0]):
            result[i[2]-1][i[3]-1+j] = 1
    else:
        for j in range(i[0]):
            result[i[2]-1+j][i[3]-1] = 1

for i in result:
    for j in i:
        print(j, end=" ")
    print()