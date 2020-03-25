h, m = input().split()
before = int(m) - 30
if(before >= 0):
    print("{0} {1}".format(h, before))
else:
    if(int(h)>0):
        print("{0} {1}".format(int(h)-1, before+60))
    else:
        print("{0} {1}".format(23, before+60))
