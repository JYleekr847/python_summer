# 내장함수 

x = [1,2,3]

print(sum(x))

# 기본 인자값 함수호출시 인자를 지정해주지 않아도 기본값이 할당
def Times(a= 10, b= 20) :
	return a*b

print(Times(), Times(5))

# 키워드 인자 : 인자 이름으로 값을 전달하는 방식 
def connectURI(server, port):
	str = "http://" + server +":"+port
	return str

srv1 = connectURI("test.com","8080")
print(srv1)

# 함수호출시 인자를 가변인자로 설정할 수 있다.

def test(*args):
	print(type(args))

test(1,2)

def union2(*ar):
	res = []
	for item in ar:
		for x in item:
			if not x in res:
				res.append(x)
	return res

a = union2("HAM","EGG","SPAM")
print(a)

b = union2("gir", "generation", "gee")
print(b)

# 정의되지 않은 인자 처리하기 - ** 
def userURIBuilder(server, port, **user):
	str = "http://" +server + ":" + port+ "/?"
	for key in user.keys():
		str += key + "="+ user[key] +"&"
	return str

str1 = userURIBuilder("test.com", "8080", id ='userid', passwd = '1234')
print(str1)
str2 = userURIBuilder("test.com", "8080", id ='userid', passwd = '1234', name = 'lj', age= '20')
print(str2)

