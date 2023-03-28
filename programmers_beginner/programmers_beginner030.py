# 외계행성의 나이

# 문제 설명
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# age는 자연수입니다.
# age ≤ 1, 000
# PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.


def solution(age):
    age = str(age)
    age = age.replace('0', 'a')
    age = age.replace('1', 'b')
    age = age.replace('2', 'c')
    age = age.replace('3', 'd')
    age = age.replace('4', 'e')
    age = age.replace('5', 'f')
    age = age.replace('6', 'g')
    age = age.replace('7', 'h')
    age = age.replace('8', 'i')
    age = age.replace('9', 'j')
    return age


a = 100
print(dir(a))
print(solution(100))


def solution(age):
    age = str(age)
    answer = ''
    num_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',]

    for i in age:
        answer += num_dict[int(i)]
    return answer


print(solution(100))

# print(dir('100'))
