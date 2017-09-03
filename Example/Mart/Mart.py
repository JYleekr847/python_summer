import re

f = open('로그인 정보.txt','r')
User = f.readline()
Password = f.readline()
Money = f.readline()
User = User.rstrip()
Password = Password.rstrip()
f.close()
check = True
print("마트 관리 시스템")
while check:
    User_input = input("이름:")
    Password_input = input("비밀번호:")
    if User_input == User and Password_input == Password:
        check = False
        print("로그인에 성공했습니다.")
    else:
        check = True
        print("로그인 정보를 확인해주세요")
잔액 = 0
판매액 = 0
구매액 = 0
육류 = 0
청과류 = 0
인스턴스식품 = 0
비식품 = 0
유제류 = 0
과자류 = 0

while True:

    print("1.재고확인")
    print("2.구매")
    print("3.판매")
    print("4.마감")
    Number = input("원하는 작업을 선택하세요")
    Number = int(Number)
    if Number == 1:
        f = open('매장 정보.txt', 'r')
        print(f.read())
        f.close()
    elif Number ==2:
        f = open('매장 정보.txt', 'r')
        육류2 = input("육류:")
        청과류2 = input("청과류:")
        인스턴스식품2 = input("인스턴스식품:")
        비식품2 = input("비식품:")
        유제류2 = input("유제류:")
        과자류2 = input("과자류:")

        구매액 = 구매액 + int(육류2) + int(청과류2) + int(인스턴스식품2) + int(비식품2) + int(유제류2) + int(과자류2)
        f.readline()
        육류1 =  f.readline()
        육류1 = re.split('[:]+',육류1)
        육류 = int(육류1[1]) + int(육류2)
        print(육류)

        청과류1 =  f.readline()
        청과류1 = re.split('[:]+',청과류1)
        청과류 = int(청과류1[1]) + int(청과류2)
        print(청과류)

        인스턴스식품1 =  f.readline()
        인스턴스식품1 = re.split('[:]+',인스턴스식품1)
        인스턴스식품 = int(인스턴스식품1[1]) + int(인스턴스식품2)

        비식품1 =  f.readline()
        비식품1 = re.split('[:]+',비식품1)
        비식품 = int(비식품1[1]) + int(비식품2)

        유제류1 =  f.readline()
        유제류1 = re.split('[:]+',유제류1)
        유제류 = int(유제류1[1]) + int(유제류2)

        과자류1 =  f.readline()
        과자류1 = re.split('[:]+',과자류1)
        과자류 = int(과자류1[1]) + int(과자류2)
        print("구입완료 !!")
        f.close()
    elif Number == 3:
        print("판매")
        f = open('매장 정보.txt', 'r')
        육류2 = input("육류:")
        청과류2 = input("청과류:")
        인스턴스식품2 = input("인스턴스식품:")
        비식품2 = input("비식품:")
        유제류2 = input("유제류:")
        과자류2 = input("과자류:")

        판매액 = 판매액 + int(육류2) + int(청과류2) + int(인스턴스식품2) + int(비식품2) + int(유제류2) + int(과자류2)
        f.readline()
        육류1 =  f.readline()
        육류1 = re.split('[:]+',육류1)
        육류 = int(육류1[1]) - int(육류2)

        청과류1 =  f.readline()
        청과류1 = re.split('[:]+',청과류1)
        청과류 = int(청과류1[1]) - int(청과류2)

        인스턴스식품1 =  f.readline()
        인스턴스식품1 = re.split('[:]+',인스턴스식품1)
        인스턴스식품 = int(인스턴스식품1[1]) - int(인스턴스식품2)

        비식품1 =  f.readline()
        비식품1 = re.split('[:]+',비식품1)
        비식품 = int(비식품1[1]) - int(비식품2)

        유제류1 =  f.readline()
        유제류1 = re.split('[:]+',유제류1)
        유제류 = int(유제류1[1]) - int(유제류2)

        과자류1 =  f.readline()
        과자류1 = re.split('[:]+',과자류1)
        과자류 = int(과자류1[1]) - int(과자류2)
        print("판매완료!!")
        f.close()

    elif Number == 4:
        print("마감!!")
        f = open('매장 정보.txt', 'r+')
        잔액1 = f.readline()
        잔액1 = re.split('[:]+',잔액1)
        잔액 = int(잔액1[1]) + 판매액 - 구매액
        f.seek(0)
        f.write("잔액:"+str(잔액)+'\n')
        f.write("육류:"+str(육류)+'\n')
        f.write("청과류:"+str(청과류)+'\n')
        f.write("인스턴스식품:"+str(인스턴스식품)+'\n')
        f.write("비식품:"+str(비식품)+'\n')
        f.write("유제류:"+str(유제류)+'\n')
        f.write("과자류:"+str(과자류)+'\n')
        break

    else:
        print("할 수 없는 기능입니다.")
