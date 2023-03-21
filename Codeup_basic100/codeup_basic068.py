num = int(input())


def score(num):
    if num >= 90:
        return 'A'
    elif num >= 70:
        return 'B'
    elif num >= 40:
        return 'C'
    else:
        return 'D'


print(score(num))
