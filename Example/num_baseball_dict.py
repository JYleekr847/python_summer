num = input("숫자를 입력하세요")
num= dict(zip(range(3),num))
ball = 0
strike = 0
while strike != 3 :
    ball = 0
    strike = 0
    num_input = input( " 숫자를 예측하세요 ")
    num_input = dict(zip(range(3),num_input))
    for i in range(3):
        for j in range(3):
            if int(num[i]) == int(num_input[j]) :
                if i == j :
                    strike = strike + 1
                else:
                    ball = ball + 1
    print("strike : {0} , ball : {1} ".format(strike,ball))
print(" 정답을 맞췄습니다")