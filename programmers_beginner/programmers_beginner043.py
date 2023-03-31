# # 문자열 정렬하기(2)
# # 문제 설명
# # 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.

# # 제한사항
# # 0 < my_string 길이 < 100

# 알파벳 소문자로 바꾸기
# 알파벳 순서대로 정렬하기
# 정렬한 알파벳 출력하기

def solution(my_string):
    answer = ''
    ord_list = []
    for i in my_string:
        # 소문자라면 ord_list에 그냥 아스키 코드로 변환해서 추가하기
        if not i.isupper():
            ord_list.append(ord(i))
        # 대문자라면 ord_list에 swapcase()를 통해서 소문자로 바꾸고
        # 아스키 코드로 변환해서 추가하기
        elif i.isupper():
            i = i.swapcase()
            ord_list.append(ord(i))
    # sort()를 통해서 리스트를 오름차순으로 정렬
    ord_list.sort()
    # 정렬한 ord_list를 for문으로
    # 아스키 코드에서 다시 변환해서 answer에 집어넣기
    for i in ord_list:
        i = chr(i)
        answer += i
    return answer


print(solution('Bcad'))

# print(ord('a'))


def solution(my_string):
    answer = ''
    ord_list = []
    for i in my_string:
        # 소문자라면 ord_list에 그냥 추가하기
        if not i.isupper():
            ord_list.append(i)
        # 대문자라면 ord_list에 swapcase()를 통해서 소문자로 바꾸기
        elif i.isupper():
            i = i.swapcase()
            ord_list.append(i)
    # sorted()를 통해서 리스트를 오름차순으로 정렬
    sort_list = sorted(ord_list)
    # 정렬한 ord_list를 for문으로 answer에 집어넣기
    for i in sort_list:
        answer += i
    return answer


print(solution('Bcad'))
