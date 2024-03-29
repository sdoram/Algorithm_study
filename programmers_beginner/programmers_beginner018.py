# 세균 증식

# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
# t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 10
# 1 ≤ t ≤ 15

def solution(n, t):
    while t > 0:
        t -= 1
        n *= 2
    return n
# 시간마다 *2하고 시간을 t -= 1로 카운트
# 필요없는 answer 삭제
# 점수도 +1점 기분도 +1


print(solution(10, 5))
