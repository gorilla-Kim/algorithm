currentTime, score = input().split()
restTime = 90 - int(currentTime)

print("{0}".format( restTime//5+int(score) if restTime%5==0 else restTime//5+int(score)+1))
