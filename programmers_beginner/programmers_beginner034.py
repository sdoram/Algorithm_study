# 최빈값 구하기
# 문제 설명
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000

def solution(array):
    answer = 0
    array_dict = {}
    for i in array:
        # array_dict에 중복 값이 없으면 value는 1, 중복 값이 있으면 +=1
        if i not in array_dict:
            # array_dict[i] = key, 1 = value
            array_dict[i] = 1
        else:
            array_dict[i] += 1

    # dict에서 value가 제일 큰 것의 key값 출력
    # reverse로 가장 큰값을 앞으로 보내고 item[1]로 뽑기 item[0] = key,[1] = value
    #   item[1]은 value를 기준으로 reverse해서 큰 값으로 정렬
    sorted_check = sorted(array_dict.items(), reverse=True,
                          key=lambda item: item[1])
    # 들어온 값이 2종류 이상이면 if문 진입
    if len(sorted_check) > 1:
        # 가장 큰 값과 두번째 값을 비교해서 다르면 if문 진입
        if sorted_check[0][1] != sorted_check[1][1]:
            answer = sorted_check[0][0]
        else:
            answer -= 1
    else:
        answer = sorted_check[0][0]
    return answer


a = [1, 2, 3, 4, 3, 3, 2]
print(solution(a))


def solution(array):
    a = []
    arr = list(set(array))
    for i in arr:
        a.append([array.count(i), i])
    a.sort(reverse=True)
    if len(a) == 1:
        answer = a[0][1]
    elif a[0][0] == a[1][0]:
        answer = -1
    else:
        answer = a[0][1]
    return answer


a = [2]
print(solution(a))
