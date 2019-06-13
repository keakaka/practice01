# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만원, 만원, 오천원, 천원, 500원, 100원, 50원, 10원, 1원
# 각 몇 개로 변환 되는지 작성하시오.

import sys, math

money = input('금액 : ')
if money.isdigit():
    money = int(money)
    for won in [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]:
        if money > won and money > 0:
            print(won, '원 : ', math.trunc(money/won), '개')
            money -= (won*math.trunc(money/won))
else:
    print('정수가 아닙니다.')
    sys.exit(0)
