ran = range(2,6)
idx = range(1,10)

for i in idx:
    for j in ran:
        print("{0} x {1} = %2d".format(j, i)%(j*i), end="\t")
    print()