# if 문 : 조건을 평가해 결과가 수행 여부를 결정

value = 10 
if value > 5 : 
	print("value is bigger than 5")

# 2개 이상의 조건 elif 사용 

score = int(input(('Input Score: ')))
if 90 <= score <= 100 :
	grade = 'A'

elif 80<= score<90 :
	grade = 'B'
elif 70<=score<80 :
	grade = 'C'
elif 60<=score<70 :
	grade = 'D'
else :
	grade = 'F'

print("grade is " + grade)


# 조건식의 참 / 거짓 판단 : bool 

print(bool(True))
print(bool(13))
print(bool(0.0))
print(bool(''))

# 예외 발생 코드 

a = 0 
if a and 10 / a :
	print("a가 0입니다")
else:
	print("에러 없음")


