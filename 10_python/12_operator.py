# 연산자 : 산술, 논리, 관계

a = 3
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

#논리연산자

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Short-Circuit

if True or a / 0: # or 인 경우 뒤에걸 볼 필요가 없다
    print('Short-Circuit Yes')
else :
    print('short-circuit no')