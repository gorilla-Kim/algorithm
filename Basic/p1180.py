i = input()
data = list(i)
k = data[len(data)-2]
data[len(data)-2] = data[len(data)-1]
data[len(data)-1] = k
result = int(data[len(data)-2] + data[len(data)-1])*2%100

print("{0}\n{1}".format(result,"GOOD" if result<=50 else "OH MY GOD"))