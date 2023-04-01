# 최댓값과 최솟값
# 문제 설명
# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

# 제한 조건
# s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

# def solution(s):
#     answer = ''
#     num_list = []

#     for count, val in enumerate(s):
#         # i가 space가 아니라면
#         if not val.isspace():
#             # 현재 value가 숫자고 이전 value는 숫자가 아니면
#             if val.isdigit() and s[count-1] == '-':
#                 # append(이전 value + 현재 밸류)
#                 num_list.append(s[count-1] + val)
#                 # 현재 밸류가 숫자면
#             elif val.isdigit():
#                 num_list.append(val)

#     # 내림차순 정렬
#     # 가장 작은 수 pop()
#     num_list.reverse()
#     min_num = num_list.pop()

#     # 오름차순 정렬
#     # 가장 큰 수 pop()
#     num_list.reverse()
#     max_num = num_list.pop()

#     if int(min_num) > int(max_num):
#         answer += max_num
#         answer += ' '
#         answer += min_num
#     else:
#         answer += min_num
#         answer += ' '
#         answer += max_num

#     return answer

def solution(s):
    answer = ''
    # 공백을 기준으로 숫자 나누기
    s_list = s.split(' ')
    int_list = []
    # int형으로 집어 넣음
    for n in s_list:
        int_list.append(int(n))

    # 최댓값 추출
    int_list.sort()
    max_num = int_list.pop()

    # 최솟값 추출
    int_list.reverse()
    min_num = int_list.pop()

    # answer에 집어 넣기
    answer += str(min_num)
    answer += ' '
    answer += str(max_num)

    return answer


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
# print(solution('-1 -2 -3 4'))
# print(solution('1,1,1,1,10'))
