# 분수의 덧셈

# 문제 설명
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
# 두 분수를 더한 값을 기약 분수로 나타냈을 때
# 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 0 <numer1, denom1, numer2, denom2 < 1,000

from fractions import Fraction


def solution(numer1, denom1, numer2, denom2):
    answer = []
    fraction = Fraction(numer1 / denom1) + Fraction(numer2 / denom2)
    answer.append(fraction.numerator)
    answer.append(fraction.denominator)
    return answer


print(solution(9, 2, 1, 3))
