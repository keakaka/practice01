# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

import math, sys

avglist = []
number = 0
for i in range(0, 5):
    number = input()
    if number.isdigit():
        avglist += [int(number)]
    else:
        print('정수만 입력하세요')
        sys.exit(0)

print(math.fsum(avglist))