# 약수의 합

# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수,
# solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

def solution(n):
    answer = n
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            answer += i
    return answer


# 제곱근으로 구하는건 이해 못하겠고
# 지금은 n/2가 이해하면서 사용가능한 최선이다.
print(solution(12))
