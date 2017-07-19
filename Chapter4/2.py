# while 문 : 조건식이 참인 동안 반복해 내부 블록의 구문을 수행한다.
# 조건식이 평가되고 내부블록 구문이 수행되고 이후도 계속해서 조건식 평가후 내부블록 수행이 반복된다.

value = 5
while value > 0 :
	print(value)
	value -= 1

# for 문 : 인자로 받은 시쿼느 객체를 아이템에 할당한다. 할당받은 아이템을 이용하여  블록구문을 수행한다.

list = ['Apple', 100 , 15.23] 
for i in list:
	print(i, type(i))

d = {"Apple":100, "Orange":200, "Banana":300}
for k, v in d.items():
	print(k,v)

list = [10, 20 ,30] 
iterator = iter(list)
for i in iterator:
	print(i)


# 예제 구구단 출력
for n in [2,3,4,5,6,7,8,9]:
	print("{0} 단".format(n))
	for i in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(n, i, n*i))
# break, continue , else

#break : 반복문 순회 도주 break 문을 만나면 반복문의 내부 블록을 벗어난다.
list = [1,2,3,4,5,6,7,8,9]
for i in list:
	if i >5 :
		break
	print("Item: {0}".format(i))
# continue : 반복문 순회 도중 continue문을 만나면 continue 문 이후의 반복문 내부블록을 수행하지않고 
# 다음 아이템을 선택하여 반복문 내부블럭을 실행한다. 

list : [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
	if i%2 ==0 :
		continue
	print("Item: {0}".format(i))
else: 
	print("Exit without break")
print("Always this is printed")

