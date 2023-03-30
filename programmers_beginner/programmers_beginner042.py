# 숫자 찾기
# 문제 설명
# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 - 1을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < num < 1, 000, 000
# 0 ≤ k < 10
# num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.


def solution(num, k):
    answer = 0
    count = 0
    num = str(num)
    # k가 num에 없을 경우 -1 출력
    if str(k) not in num:
        answer = -1
        return answer
    # k가 있는 경우 num에서 k의 자릿수 찾기
    for n in num:
        count += 1
        if int(n) == k:
            print(n)
            answer = count
            break

    return answer


print(solution(29183, 1))
