#람다 함수 : 함수의 이름은 존재하지 않고 객체만존재하는 익명함수 한줄을 실행한결과가 바로 출력된다.
g = lambda x,y : x*y
print(g(2,3))
a = (lambda x : x*x)(3)
print(a)