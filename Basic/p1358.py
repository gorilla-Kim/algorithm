# 입력된 값이 무조건 홀수이다라는 가정
n = int(input())
center = int((n+1)/2)

for i in range(1, center+1):
    center -= 1
    print(" "*center, end="")
    print("*" *( 1 if i==1 else 1+(i-1)*2))