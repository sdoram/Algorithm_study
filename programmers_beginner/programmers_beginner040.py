# 인덱스 바꾸기
# 문제 설명
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 < my_string의 길이 < 100
# 0 ≤ num1, num2 < my_string의 길이
# my_string은 소문자로 이루어져 있습니다.
# num1 ≠ num2
def solution(my_string, num1, num2):
    answer = ''
    string_list = list(my_string)
    # 바꿔줄 단어 찾기
    str_num1 = my_string[num2]
    str_num2 = my_string[num1]
    # 바꿀 단어 리스트에서 바꾸기
    string_list[num1] = str_num1
    string_list[num2] = str_num2
    # answer에 리스트 풀어서 담기
    for str_ in string_list:
        answer += str_
    return answer


print(solution('hello', 1, 2))
