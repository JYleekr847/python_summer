# 상속
class Person:
	" 부모 클래스"
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber
	
	def PrintInfo(self):
		print("Info(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))

	def PrintPersonData(self):
		print("Person(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))

class Student(Person):
	def __init__(self, name, phoneNumber, subject, studentID):
		self.Name = name
		self.PhoneNumber = phoneNumber
		self.Subject = subject
		self.StudentID = studentID


p = Person("Derick","010-123-4567")
print(p.__dict__)

s = Student("Marry", "010-654-3210", "Computer science", "9900900")
s.__dict__