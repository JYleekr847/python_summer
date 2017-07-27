# 클래스 선언 

class MyClass:
	"""아주 간단한 클래스"""
	pass
print(dir())
print(type(MyClass))


class Person:
	Name = "Defalut Name"
	def Print(self):
		print("My Name is {0}".format(self.Name))
p1 = Person()
p1.Print()
p1.Name = " 내 이름은 김연아!"
p1.Print()

# 파이썬에서 기본접근 권한은 public이다.
# self 인자는 현재 인스턴스 객체를 가리키는 것이다.