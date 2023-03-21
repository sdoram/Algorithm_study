def solution(n):
    answer = 0
    if n % 2 == 0:
        answer += n

    while n > 0:
        n -= 1
        if n % 2 == 0:
            answer += n
    return answer


print(solution(10))
