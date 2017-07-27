# filter(<function> | none, <이터레이션 가능한 자료형>)

List = [10,25,30]

IterL = filter(None,List) # 필터링 기준이 되는 함수 X

for i in IterL:
	print("Item:{0}".format(i))

def GetBiggerThan20(i) : 
	return i > 20 

a = GetBiggerThan20(25)
print(a)

	
IterL = filter(GetBiggerThan20, List)

for i in IterL:
	print("item:{0}".format(i))

NewL = list(filter(GetBiggerThan20,List))

print(NewL)

IterL = filter(lambda i: i>20, List)

for i in IterL:
	print("item:{0}".format(i))

#zip()함수를 이용하여 3개이상의 시퀀스 형이나 이터레이터형 객체를 튜플 형태로 서로 쌍을 묶을 수 있다.

X = [10,20,30]

Y = ['A', 'B', 'C']

for i in zip(X,Y):
	print("Item:{0}".format(i))

RetList = list(zip(X,Y))
print(RetList)

X = [10,20,30]
Y = "ABC"
Z = (1.5 , 2.5, 3.5)

RetList1 = list(zip(X,Y,Z))
print(RetList1)

#map() 함수 : 첫 인자로 함수 이름이온다. 뒤의 인자는 순회 가능한 객체 

List2 = [1,2,3]
def Add10(i):
	return i + 10

for i in map(Add10, List2):
	print("Item: {0}".format(i))

RetList2 = list(map((lambda i : i+10), List2))
print(RetList2)

# pow 함수를 이용한 예제 

X = [1,2,3]
Y = [2,3,4]

RetList3 = list(map(pow,X,Y))

print(RetList3)

# 효율적인 순회 방법
# 일반적인 방법

L  = ['Apple', 'Orange', 'Banana']
for i in L:
	print(i)

# join()이나 리스트 내장을 이용한 효율적인 방법 => join을 이용하면 print 함수가 1번만 호출된다.

print("\n".join(L))
print("\n".join(i for i in L))


# 성능 비교 

import time 

l= range(1000)

t = time.mktime(time.localtime())
for i in l:
	print(i, )
t1 = time.mktime(time.localtime()) - t 

t = time.mktime(time.localtime())
print(", ".join(str(i) for i in l))
t2 = time.mktime(time.localtime()) - t

print("for 문으로 각인자를 출력")
print("Take {0} seconds".format(t1))

print("join 문으로 각 인자를 출력")
print("Take {0} seconds".format(t2))

	