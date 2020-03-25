a,b,c,d = input().split()
result = (int(a)*int(b)*int(c)*int(d))/(8*1024*1024)
print("{0} MB".format(round(result,1)))