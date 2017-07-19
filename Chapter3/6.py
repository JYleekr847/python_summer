# 재귀적 함수호출 : 함수 내부에서 자기 자신을 호출하는 것 
def factorial(x):
	if x == 1:
		return 1
	return x*factorial(x-1)
a = factorial(10)
print(a)

def hanoi(ndisks, startPage = 1,endPage = 3):
	if ndisks:
		hanoi(ndisks -1, startPage ,6- startPage- endPage)
		print(startPage, "번 기둥의", ndisks, "번 원반을",endPage, "번 기둥에 옮깁니다.")
		hanoi(ndisks - 1, 6-startPage-endPage, endPage)

hanoi(ndisks=3)


# pass : 아무런 동작도 수행하지 않는다. 빈 클래스나 빈 모듈, 함수를 만들때 사용
# __doc__ 속성은 부모객체에 대한 설명을 적을 때 사용된다.

def plus(a,b):
	return a + b
plus.__doc__ = "return the sum of parameter a,b"
help(plus)

