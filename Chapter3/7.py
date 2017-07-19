# 이터레이터 : 리스트 , 튜플, 문자열 같은 객체에는 이터레이터라는 특별한 객체가 포함되어 있다.
for element in [1,2,3]:
	print(element)
for element in (1,2,3):
	print(element)
for key in {'one' :1, 'two':2}:
	print(key)
for char in "123":
	print(char)


s = 'abc'
it = iter(s)
print(next(it))
print(it.__next__())

# 제너레이터 : 이터레이터를 만드는 간단하고 강력한 도구
# yield를 입력하면 함수를 호출한 곳에 값을 전달하고 함수를 종료하지 않습니다.

def reverse(data):
	for index in range(len(data) -1, -1, -1):
		yield data[index]
for char in reverse('golf'):
	print(char)

# yield를 사용하지 않았을 때 , 첫번째 문자열을 내뱉고 두번째 호출에서는 함수가 종료되어 
# 에러가 발생한다.

def abc():
	data = "abc"
	for char in data:
		return char

it = iter(abc())
print(next(it))

# 제너레이터를 이용  : 함수 상태를 보존하고 다시 호출될 수 있다. 
# 이터레이터를 만들때 사용하면 매우 강력한 도구가 될 수 있다. 또한 메모리가 절약될 수 있다.
def abc(): 
	data = "abc"
	for char in data:
		yield char 
print(abc)
it = iter(abc())
print(next(it))
print(next(it))
print(next(it))


# 제너레이터를 이용한 피보나치 수열

def fibonacci():
	a, b = 0,1
	while 1:
		yield a
		a,b = b, a+b
for i, ret in enumerate(fibonacci()):
	if i < 20: print(i, ret)
	else: break
