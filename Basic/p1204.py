strlist = {1:"st", 2:"nd", 3:"rd", 4:"th"}

num = input()
if((int(num)//10)==1 ):
    print(num+strlist[4])
else:
    print("{0}{1}".format(num, strlist[int(num)%10 if int(num)%10<4 and int(num)%10!=0 else 4]))
