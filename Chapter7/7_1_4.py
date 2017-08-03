def divide(a,b):
	return a/b
try:
	c= divide(5,"af")
except TypeError as e:
	print(" 에러: ", e.args[0])
except:
	print(" 무슨에러인지 알 수 없습니다")
