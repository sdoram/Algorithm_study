# 암호 해독

# 문자열 cipher와 정수 code가 매개변수로 주어질 때
# 해독된 암호 문자열을 return하도록
# solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ cipher의 길이 ≤ 1,000
# 1 ≤ code ≤ cipher의 길이
# cipher는 소문자와 공백으로만 구성되어 있습니다.
# 공백도 하나의 문자로 취급합니다.

def solution(cipher, code):
    return (cipher[code-1::code])

# slice끝 설정하는 부분 지우기 <- 없으면 끝까지 실행
# 0번부터 시작이므로 -1로 처음에 0번을 카운트 하기


print(solution("dfjardstddetckdaccccdegk", 4))
