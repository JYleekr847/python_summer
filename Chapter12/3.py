#분수모듈
import math
import fractions
a = fractions.Fraction(4, 16)
print(a)
b = fractions.Fraction(-6,21)
print(b)
c = fractions.Fraction(3)
print(c)

a2 = fractions.Fraction(a)
print(a2)

print(fractions.Fraction('6/21'))
print(fractions.Fraction('3.14'))
print(fractions.Fraction("-0.34"))

s = """
-0.34
"""

print(fractions.Fraction(s))

from fractions import Fraction
print(Fraction.from_float(0.5)) # 실수를 받아 Fraction 객체 생성
print(Fraction.from_decimal(4)) # 10진수를 받아 Fraction 객체생성

from math import pi,cos
from fractions import Fraction
print(Fraction.from_float(pi))
print(Fraction.from_float(pi).limit_denominator(100))

# 최대공약수를 반환하는  gcd() 클래스 메서드

print(fractions.gcd(120,180))
print(fractions.gcd(0.5,6))
