# 배열의 유사도
# 문제 설명
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ s1, s2의 길이 ≤ 100
# 1 ≤ s1, s2의 원소의 길이 ≤ 10
# s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
# s1과 s2는 각각 중복된 원소를 갖지 않습니다.

def solution(s1, s2):
    answer = 0
    for i in s1:
        for s in s2:
            if i == s:
                answer += 1

    return answer


def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1

    return answer


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
