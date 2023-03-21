input_month = int(input())

if (input_month / 3) >= 1 and (input_month / 3) < 2:
    print('spring')
elif (input_month / 3) >= 2 and (input_month / 3) < 3:
    print('summer')
elif (input_month / 3) >= 3 and (input_month / 3) < 4:
    print('fall')
# 13이상의 정수 입력시 or 음수 입력시 출력
elif input_month > 12 or input_month < 0:
    print(f'{input_month}는 올바른 값이 아닙니다.')
elif (input_month / 3) == 4 or (input_month / 3) < 1:
    print('winter')
# else:
    # print('winter')
