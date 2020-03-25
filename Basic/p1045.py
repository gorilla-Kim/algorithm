a, b = input().split()
a = int(a)
b = int(b)
div = str(round(a/b, 2))
if ( len(div) <= 3 ):
    div = div+'0'
print("{0}\n{1}\n{2}\n{3}\n{4}\n{5}".format(a+b, a-b, a*b, a//b, a%b, div))