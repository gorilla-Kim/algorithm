a = input()
for i in range(1, 16):
    result = "{0}*{1}=%0x".format(a, i if i<10 else chr(i+55)) % ((ord(a)-55)*i)
    print(result.upper())