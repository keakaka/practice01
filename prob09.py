# 주어진 if 문을 dict를 사용해서 수정하세요.
import collections

menu = input('메뉴: ')
if menu == '오뎅' or menu == '순대' or menu == '만두':
    prices = {'오뎅': 300, '순대': 400, '만두': 500}
else:
    prices = collections.defaultdict(int)


print('가격: {0}'.format(prices[menu]))
