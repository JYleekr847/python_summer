class Person:
	name = "Default Name"

p1 = Person()
p2 = Person()

p1.name = "김연아"
print("p1`s name: ", p1.name)
print("p2`s name: ", p2.name)

# p1의 멤버데이터 name 는 데이터가 변경되면서 p1의 인스턴스에 변경된 데이터가 저장
# 또한 변경된 데이터를 참조하여 name 값을 가져온다
# p2는 데이터의 변경이 없으므로 클래스 객체의 데이터를 참조하여 name을 가져온다

p1.age = 20
print("p1`s age: ", p1.age)

# 동적으로 멤버변수를 추가/삭제 할 수 있다.


str = " NOT Class Member"
class GString:
	str=""
	def Set(self, msg):
		self.str = msg
	def Print(self):
		print(self.str)

g = GString()
g.Set("First Message")
g.Print()

# 클래스 객체의 데이터 변경은 __class__ 를 사용한다.

class Test:
	data = "Default"

i2 = Test()
i1 = Test()

i1.__class__.data = "클래스 데이터가 변경됩니다."
print(i1.data)
print(i2.data)

i2.data = "i2 데이터가 변경됩니다"
print(i1.data) # 인스턴스에서 변수를 변동하지 않았으므로 클래스 객체값 참조
print(i2.data) # 인스턴스의 값이 변경되어서 저장된 값을 참조함
print(i2.__class__.data) # 클래스 객체의 데이터는 변하지 않음 



