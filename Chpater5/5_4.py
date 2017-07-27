# 클래스 객체와 인스턴스 객체의 관계

class Person:
	pass
class Bird:
	pass
class Student(Person): # Person을 상속받음
	pass

p, s = Person(), Student()
print("p is instance of Person:" , isinstance(p, Person))
print("s is instance of Person:" , isinstance(s, Person))
print("p is instance of object:" , isinstance(p, object))
print("p is instance of Bird:" , isinstance(p, Bird))
print("int is instance of object:", isinstance(int, object))


# isinstance(인스턴스 객체, 클래스 객체) : True or False 상속관계에 있어도 True로 반환한다.