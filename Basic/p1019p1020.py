# -*- encoding: utf-8 -*-

# 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
# 파이썬 2의 raw_input 함수는 모든 입력값을 문자열 타입으로 받습니다.
a = input("Please insert year, month, day.\(.seperated dot\)\n(insert): ").split('.')
print('%04d.%02d.%02d'%(int(a[0]),int(a[1]),int(a[2])))
# 1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
b, c = input().split('-')
print("%06d%07d"%(int(b),int(c)))