# 연산자 중복 정의

class GString:
	def __init__(self, init =None):
		self.content = init
	def __sub__(self, str):
		for i in str:
			self.content = self.content.replace(i, '')
		return GString(self.content)
	def Remove(self, str):
		return self.__sub__(str)

g =GString("ABCDEFGabcdefg")

g - "Adg"
print(g.content)


class GString2:
	def __init__(self, init=None):
		self.content = init
	def __sub__(self, str):
		for i in str:
			self.content = self.content.replace(i, '')
		return GString2(self.content)
	
	def __abs__(self):
		return GString2(self.content.upper())

	def Print(self):
		print(self.content)

g = GString2("aBcdef")
g -="df"
g.Print()
g = abs(g)
g.Print()


class GString3:
	def __init__(self, init = None):
		self.content = init
	def __sub__(self, str):
		print("- operator is called!")
		for i in str:
			self.content = self.content.replace(i,'')
		return GString2(self.content)
	def __isub__(self, str):
		print("-= operator is called!")
		for i in str:
			self.content = self.content.replace(i,'')
		return GString2(self.content)

g = GString3("aBcdef")
print(g.content)
g - "a"
print(g.content)
g -= "Bc"
print(g.content)


# 시퀀스형 연산자

class Sequencer:
	def __init__(self, maxValue):
		self.maxValue = maxValue
	def __len__(self):
		return self.maxValue
	def __getitem__(self, index):
		if 0<index<=self.maxValue:
			return index*10
		else:
			raise IndexError("Index out of Range")
	def __contains__(self, item):
		return 0 < item <= self.maxValue

s = Sequencer(5)
print(s[1])
print(s[3])

print([s[i] for i in range(1,6)])
print(len(s))
print(3 in s )
print(7 in s)
print(s[7])
