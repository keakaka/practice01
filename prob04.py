# 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)

for su in range(1, 10):
    for dan in range(2, 10):
        print(dan, ' X ', su, ' = ', dan*su, end='\t\t')

    print('')
