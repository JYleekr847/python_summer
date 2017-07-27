# 정적 메서드, 클래스 메서드

class CounterManager:
	insCount = 0
	def __init__(self):
		CounterManager.insCount += 1
	def printInstanceCount():
		print("Instance Count:", CounterManager.insCount)
a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.printInstanceCount()

# printInstanceCount 함수에서 self를 사용하지 않음으로써 암묵적으로 클래스 영역을 참조한다고 나타냈다.
# 인스턴스 영역에서 접근할 때 에러가 뜨는 것을 확인할 수 있다.


class CounterManager2:
	insCount = 0
	def __init__(self):
		CounterManager2.insCount += 1
	def staticPrintCount():
		print("Instance Count:", CounterManager2.insCount)
	SPrintCount = staticmethod(staticPrintCount)

	def classPrintCount(cls):
		print("Instance Count:", cls.insCount)
	CPrintCount = classmethod(classPrintCount)

a, b, c = CounterManager2(), CounterManager2(), CounterManager2()

CounterManager2.SPrintCount()
b.SPrintCount()

CounterManager2.CPrintCount()
b.CPrintCount()

# python에서는 정보은닉을 위해서 __[멤버이름]으로 변수를 선언함으로써 외부에서 접근을 못하도록 설정하였습니다.

class CounterManager3:
	__insCount = 0
	def __init__(self):
		CounterManager3.__insCount += 1
	def staticPrintCount():
		print("Instance Count: %d" %CounterManager3.__insCount)
	SPrintCount = staticmethod(staticPrintCount)

a, b, c= CounterManager3(),CounterManager3(),CounterManager3()

CounterManager3.SPrintCount()

