# 짝수의 합

# 문제 설명
# 정수 n이 주어질 때,n이하의 짝수를 모두 더한 값을
# return 하도록 solution 함수를 작성해주세요.


# 제한사항
# 0 < n ≤ 1000

def solution(n):
    answer = 0
    if n % 2 == 0:
        answer += n

    while n > 0:
        n -= 1
        if n % 2 == 0:
            answer += n
    return answer


def solution2(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer


print(solution(10))
print(solution2(10))
