def Times(a,b):
	return a*b
print(Times(10,10))

# 함수의 레퍼런스를 다른 변수에 할당하게 되면 함수 객체가 복사되는 것이 아니라 레퍼런스만 복사되는것(얕은 복사)
myTimes = Times

#위와 같은 경우에는 myTimes와 Times가 같은 함수 객체를 가리키게 된다.

r = myTimes(10,10)
print(r)

# return은 반환값으로 오직 한개의 객체만 반환가능하다. 튜플을 이용하여 여러개를 동시에 반환하는 것처럼 보이기도 한다.

def swap(x,y):
	return y,x
print(swap(1,2))
a, b = swap(1,2)
print(a, b)
x= swap(1,2)
print(type(x)) 
	

def intersect(prelist, postlist):
	retList = []
	for x in prelist:
		if x in postlist and x not in retList:
			retList.append(x)
	return retList
list1 = "SPAM"
list2 = "EGG"
is1 = intersect(list1, list2)
print(is1)
is2 = intersect(list1, ['H','A','M'])
print(is2)
tuple1 = ('B' , 'E', 'E', 'F')
is3 = intersect(list2, tuple1)
print(is3)


