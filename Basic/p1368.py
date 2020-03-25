h, k, d = input().split()

# 세로
for i in range(0, int(h)):
    # 가로
    print(" "*i if d=="L" else " "*(int(h)-1-i), end="")
    print("*"*int(k))