# 영어가 싫어요

# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
# 문자열 numbers가 매개변수로 주어질 때, numbers를
# 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# numbers는 소문자로만 구성되어 있습니다.
# numbers는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.
# 1 ≤ numbers의 길이 ≤ 50
# "zero"는 numbers의 맨 앞에 올 수 없습니다.

def solution(numbers):
    count = 0
    num_list = [["zero", '0'], ['one', '1'], ["two", '2'], ["three", '3'], ["four", '4'],
                ["five", '5'], ["six", '6'], ["seven", '7'], ["eight", '8'], ["nine", '9']]
    while len(num_list) > count:
        numbers = numbers.replace(
            (num_list[count][0]), (num_list[count][1]))
        count += 1
    return int(numbers)


print(solution('onetwothreefourfivesixseveneightninezero'))

# len()을 numbers로 주고 있어서 런타임 에러가 발생했다.


def solution(numbers):
    num_list = [["zero", '0'], ['one', '1'], ["two", '2'], ["three", '3'], ["four", '4'],
                ["five", '5'], ["six", '6'], ["seven", '7'], ["eight", '8'], ["nine", '9']]
    for i in range(len(num_list)+1):
        numbers = numbers.replace(
            (num_list[i-1][0]), (num_list[i-1][1]))
    return int(numbers)


print(solution('onetwothreefourfivesixseveneightninezero'))
