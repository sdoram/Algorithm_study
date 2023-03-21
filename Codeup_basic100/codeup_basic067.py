a = int(input())


def even_odd(a):
    if a < 0:
        if a % 2 == 0:
            return 'A'
        else:
            return 'B'
    else:
        if a % 2 == 0:
            return 'C'
        else:
            return 'D'


print(even_odd(a))
