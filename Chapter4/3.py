# range() - 수열의 생성 range(['시작값'],'종료값',['증가값']) , 시작값과 증가값은 선택적으로 있으면 되고 종료값은 반드시 지정해야함
a = list(range(10))
print(a)
b = list(range(10,1,-1))
print(b)
c = tuple(range(1,10,2))
print(c)

#리스트 항목과 인덱스를 동시에 얻는법

for i in range(10, 20, 2):
	print(i)
List = ['Apple','Orange', 'Banana']
for i in range(len(List)):
	print("Index : {0}, Value: {1}".format(i,List[i]))

list = [100, 15.5, "Apple"]
for i , v in enumerate(list,101):
	print(i, v)

#리스트 내장 
L = [1,2,3,4,5]

list1 = [i ** 2 for i in L]
print(list1)

t = ("apple", "banana", "orange")
tuple1 = [len(t) for i in t]

print(tuple1)

d = {100:"apple", 200:"banana" , 300:"orange"}

list2= [v.upper() for v in d.values()]
print(list2)




