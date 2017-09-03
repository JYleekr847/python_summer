import math
print(math.ceil(3.14))#올림
print(math.floor(3.14))#내림
print(math.trunc(3.14))#버림

print(math.copysign(6.5,-0.0))
print(math.fabs(-6.5))
print(math.factorial(3.0))
print(math.modf(-6.5))
l = [3.14, 1.24, 5.23]
s = math.fsum(l)
print(s)

# % 연산과 fmod 연산의 차이점

f = math.fmod(5.5,  3)
print(f)
p = 5.5 % 3
print(p)
# 몫이 피제수와 일치하지 않음
f = math.fmod(-5.5, 3)
print(f)
p = -5.5 % 3
print(p)
# 정수연산에는 %, 부동소수점연산에는 fmod
