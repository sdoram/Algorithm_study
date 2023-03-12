a,b=input().split()
a=int(a)
b=int(b)
print((bool(a) and bool(b)) or (not bool(a) and not bool(b)))
# print(bool(a) == bool(b)) # 다른 사람코드인데 이게 더 간단하네