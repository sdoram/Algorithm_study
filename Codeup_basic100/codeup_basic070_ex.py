input_month = int(input())

# 3,4,5월은 3으로 1번 나눌 수 있음
if input_month//3 == 1:
    print('spring')
# 6,7,8월은 3으로 2번 나눌 수 있음
elif input_month//3 == 2:
    print('summer')
# 9,10,11월은 3으로 3번 나눌 수 있음
elif input_month//3 == 3:
    print('fall')
else:
    print('winter')
