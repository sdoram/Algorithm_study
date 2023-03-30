# 문자열 내 p와 y의 개수
# 문제 설명
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.

def solution(s):
    # 대소문자 구분 X =  한종류로 바꿔서 만들기
    str_ = s.upper()
    my_dict = {}

    # 카운트 함수
    for i in str_:
        if i in my_dict.keys():
            my_dict[i] += 1
        elif i == 'Y':
            my_dict[i] = 1
        elif i == 'P':
            my_dict[i] = 1

    # key 'P'와 'Y'의 밸류 비교
    if my_dict.get('P') == my_dict.get('Y'):
        return True
    elif my_dict.get('P') != my_dict.get('Y'):
        return False

    return True


print(solution("pPoooyY"))
print(solution("Pyy"))
print(solution("OOOOKSHJ"))
