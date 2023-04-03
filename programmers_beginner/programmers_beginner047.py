# 특정 문자 제거하기
# 문제 설명
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# letter은 길이가 1인 영문자입니다.
# my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
# 대문자와 소문자를 구분합니다.

def solution(my_string, letter):
    answer = ''
    # for문을 돌면서 if문으로 letter 걸러내기
    for i in my_string:
        # i가 letter가 아니라면
        if not i == letter:
            answer += i

    return answer
