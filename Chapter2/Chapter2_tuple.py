﻿a = {1,2,3}
b = {3,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
c = a-b
d = a | b
e = a & b
print(c,d,e)

print("여기서 부터 튜플입니다.")

t = (1,2,3)
print(type(t))
a, b = 1, 2 
print(a,b)
(a,b) = (1,2)
print(a,b)
a,b = b,a 
print(a,b)

a = set(t)
print(a)
print(type(a))
print("튜플을 세트로 변환하였습니다")
b= list(a)
print(b, type(b))
print("세트를 리스트로 변환하였습니다")
c= tuple(b)
print(c, type(c))
print("리스트를 튜플로 변환하였습니다")

a = set((1,2,3))
print(1 in a)
b = list(a)
print(2 in b)
c = tuple(b)
print(3 in c)
print(4 in a) 