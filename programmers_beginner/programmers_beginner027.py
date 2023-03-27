# 이진수 더하기

# 문제 설명
# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# return 값은 이진수를 의미하는 문자열입니다.
# 1 ≤ bin1, bin2의 길이 ≤ 10
# bin1과 bin2는 0과 1로만 이루어져 있습니다.
# bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.


def solution(bin1, bin2):
    answer = int(bin1, 2) + int(bin2, 2)
    return format(answer, 'b')


print(solution('10', '11'))


# def solution(bin1, bin2):
#     bin1 = list(bin1)
#     bin2 = list(bin2)
#     count = 0
#     answer = 0
#     while len(bin1) > 0:
#         num = bin1.pop()
#         print(bin1)
#         count += 1
#         # 첫번째가 1인지 0인지 체크
#         if num == '1' and count == 1:
#             answer += 1
#             # 두번째 부터 1인지 0인지
#         elif num == '1':
#             answer += count*2
#             print(answer)
#     return answer


# print(solution('1110', '11'))

# a = '101'
# a = list(a).pop
