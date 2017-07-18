# 파이썬에서 인자는 레퍼런스를 이용해 전달한다. 
a = 10
b= 20 

def sum1(x, y):
	return x+y
print(sum1(a,b))

#정수형 변수는 변경 불가능한 변수 
x = 10 
def sum2(x, y):
	x = 1
	return x+y
print(sum2(x,b))
print(x)

# 리스트는 변경가능한 변수타입
# 함수가 종료된뒤 함수 내에서 함수 바깥의 값을 변경시킴, x[0]는 레퍼런스가 아닌 실제값의 주소를 의미한다.
def change(x):
	x[0] ='H'
wordlist = ['J','A','M']
change(wordlist)
print(wordlist)

# 변경가능한 변수타입을 함수내에서 변경했을때 외부에 영향을 미치지 않게하는 방법 

def change2(x):
	x = x[:]
	x[0] = 'H'
	return None
wordlist = ['J','A','M']
change2(wordlist)
print(wordlist)

# 깊은 복사를 이용해 똑같은 객체를 한개 더 생성한다.
