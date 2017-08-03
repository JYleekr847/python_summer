def divide(a,b):
	return a/b

try:
	c = divide(5,2)
except ZeroDivisorError:
	print("두번째 인자는 0 이어서는 안됩니다.")
except TypeError:
	print("모든 인자는 숫자여야합니다")
except:
	print("ZeroDivisorError, TypeError를 제외한 다른 에러")
else:
	print("result:{0}".format(c))
finally:
	print("항상 finally block은 실행됩니다")