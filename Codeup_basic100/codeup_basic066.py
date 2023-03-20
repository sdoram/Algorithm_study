a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)


def even_odd(i):
    if i % 2 == 0:
        return 'even'
    else:
        return 'odd'


print(even_odd(a))
print(even_odd(b))
print(even_odd(c))
