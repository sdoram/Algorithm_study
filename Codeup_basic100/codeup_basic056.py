a,b = input().split()
a = int(a)
b = int(b)
print(not bool(a) is bool(b)) # 이렇게 풀면 나중에 문제생기나?
# print((c and (not d)) or ((not c) and d)) # 예시