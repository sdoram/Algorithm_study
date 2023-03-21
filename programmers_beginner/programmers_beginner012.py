def solution(n, k):
    answer = 0
    # 양꼬치 값
    answer += n * 12000
    # 음료 서비스
    service = n // 10
    k = k-service
    # 음료 값
    answer += k * 2000
    return answer


print(solution(10, 3))
