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
    numbers = numbers.replace('zero', '0')
    numbers = numbers.replace('one', '1')
    numbers = numbers.replace('two', '2')
    numbers = numbers.replace('three', '3')
    numbers = numbers.replace('four', '4')
    numbers = numbers.replace('five', '5')
    numbers = numbers.replace('six', '6')
    numbers = numbers.replace('seven', '7')
    numbers = numbers.replace('eight', '8')
    numbers = numbers.replace('nine', '9')
    return int(numbers)

# 조건문 걸어보려다가 멘탈 나갈뻔한 문제
# answer 삭제


print(solution('onetwothreefourfivesixseveneightninezero'))


def solution2(numbers):
    numbers = numbers.replace(
        'zero', '0').replace(
        'one', '1').replace(
        'two', '2').replace(
        'three', '3').replace(
        'four', '4').replace(
        'five', '5').replace(
        'six', '6').replace(
        'seven', '7').replace(
        'eight', '8').replace(
        'nine', '9')
    return int(numbers)

# 이렇게 써도 어지럽네


print(solution2('onetwothreefourfivesixseveneightninezero'))
