# 생성자 , 소멸자 
class  MyClass:
	def __init__(self, value):
		self.Value = value
		print("Class is created ! Value = ", value)
	def __del__(self):
		print("Class is deleted ! ")

def foo():
	d = MyClass(10)

foo()


c= MyClass(10) #레퍼런스 카운터 1
c_copy = c  # 레퍼런스 카운터 2
del c	# 레퍼런스 카운터 1
del c_copy # 레퍼런스 카운터 0