# 스코핑 룰 

a = [1,2,3] 
def scoping():
	a = [4,5,6]

# 이름 공간 : 프로그램에서 쓰이는 이름이 저장되는 공간 위에서는 a가 저장되는 공간
#위에서 변수를 선언하면 [1,2,3]이라는 객체가 메모리공간에 생성되고 , a라는 이름을 가진 레퍼런스가 가리키고 있다.

# 함수는 별도의 이름공간을 갖는다 . 함수 내부에서 사용되는 변수는 함수 내부의 이름공간을 참조한다. 
# 하지만 함수내부(지역 영역)에서 이름을 찾지 못하게 되면 상위 공간(전역 영역)에서 이름을 찾는다. 

x = 1

def func(a):
	return a + x 

print(func(1))
#함수 내부에서 x라는 변수를 찾지못해 전역영역에 있는 x  = 1을 참조해 값을 반환

def func2(a):
	x=2
	return a+x

print(func(2))

#함수 내부에 x가 존재하여 함수내부의 x값을 참조하여 값을 반환 


#이름을 검색하는 순서  L G B : Local Global Built-in

g = 1
def testScope(a) : 
	global g
	g = 2 
	return g + a 

print(testScope(1))
print(g)