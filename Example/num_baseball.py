num = input("숫자를 입력하세요")
ball = 0
strike = 0 


while True:
    num_input = input( " 숫자를 예측하세요 ")
    for i in range(3):
        for j in range(3):
            if int(num[i]) == int(num_input[j]) :
                if i == j :
                    strike = strike + 1
                else:
                    ball = ball + 1

    print("strike : {0} , ball : {1} ".format(strike,ball))
    if strike == 3:
        break
    ball = 0
    strike = 0

print(" 정답을 맞췄습니다")
