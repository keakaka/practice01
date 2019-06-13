# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

count = 0
mysum = 0
for i in [3, 6, 9]:
    if i % 3 == 0:
        count += 1
        mysum += i

print('주어진 리스트에서 3의 배수의 개수 = >', count)
print('주어진 리스트에서 3의 배수의 합 = >', mysum)