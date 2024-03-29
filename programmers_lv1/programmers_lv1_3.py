# 자릿수 더하기

# 자연수 N이 주어지면,
# N의 각 자릿수의 합을 구해서 return 하는
# solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    answer = 0
    n = str(n)
    n = list(n)
    while len(n) > 0:
        answer += int(n.pop())
    return answer


print(solution(123))


def solution(n):
    answer = 0
    n = str(n)
    for i in range(1, len(n)+1):
        answer += int(n[i-1:i])
    return answer


print(solution(123))
