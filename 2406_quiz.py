# id_number = "040712"
#
# print(id_number[0:2])  # 0부터 2직전까지
# print(id_number[2:6])
# print(int(id_number[0:2]) + int(id_number[2:6]))
#
# phone_number = "02-1234-5678".split("-")
# print(phone_number[0] + "\n" + phone_number[2])
import math

2-1
#학번을 student_number변수에 넣고, 학급을 출력하고, 학과를 출력하기
#반이 0미만이거나 7이상이면 "잘못입력했습니다."출력하기
#student_number ='2100' 또는 '2000'
#<출력예시>   1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
'''
student_number='2406'
if student_number[1]=="1":
    print("1반 뉴미디어소프트웨어과")
elif student_number[1]=="2":
    print("2반 뉴미디어소프트웨어과")
elif student_number[1]=="3":
    print("3반 뉴미디어웹솔루션과")
elif student_number[1]=='4':
    print("4반 뉴미디어웹솔루션과")
elif student_number[1]=='5':
    print("5반 뉴미디어디자인과")
elif student_number[1]=="6":
    print("6반 뉴미디어디자인과")
else:print("잘못입력했습니다.")

student_number='2406'
number = student_number[1]
number = int(number)
majors = ['0', '솦과', '웹과', '뉴디']
if 1 <= number and number <= 6:
    print(f"{number}반 {majors[(number-1)//2]} ")
else:
    print("잘못입력했습니다.")
'''
#2-2
#학번을 함수인 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
#함수호출
#grade, major = get_major("2100")
#print(major,grade) #뉴미디어소프트웨어과2
'''
def get_major(argumenet):
    if argumenet[1]=="1" or argumenet[1]=="2":
        major="뉴미디어소프트웨어과"
        return argumenet[0],major
    elif argumenet[1]=="3" or argumenet[1]=="4":
        major="뉴미디어웹솔루션과"
        return argumenet[0],major
    elif argumenet[1]=="5" or argumenet[1]=="6":
        major="뉴미디어디자인과"
        return argumenet[0],major

grade,major=get_major("2406")
print(major,grade)

print('---------------------------')

def get_major(student_number):
    majors = ['소', '소', '솔', '솔', '디', '디']
    grade = student_number[0]
    classroom = student_number[1]
    classroom = int(student_number[1])
    return grade, majors[classroom-1]

grade, major = get_major('2406')
print(major, grade)
'''


#3-3
#인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면
#그 인수들의 평균을 구하여 리턴하는 함수 만들기
#<함수호출>
#print(average(10,20,30)) #20.0
#print(average(4,23)) #13.5
'''
def average(*number):
    sum=0
    for i in number:
        sum+=i
        i+=1
    average=(sum/len(number))
    print(average)


print(average(10,20,30))
print(average(4,23))

def average(*numbers):
    count = 0
    sum_value = 0
    for number in numbers:
        sum_value += number
        count += 1
    return  sum_value/count

def average(*numbers):
    return sum(numbers)/len(numbers)  # len 길이 재는것

print(average(10, 20, 30)) # 큐플
print(average(4, 23))

'''

#2-4
#키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI지수를 리턴하는 함수 만들기
#(소수 첫째자리까지 반올림)

#*BMI지수 계산법 : 체중(kg) / 키의 제곱
#18.5 미만 : 저체중
#18.5이상 23 미만 : 보통
#23 이상 25 미만 : 과체중
#25이상 : 비만

#<함수호출>
#bmi = get_bmi(176,69)
#print(bmi) #22.3
'''
def get_bmi(height, weight):
    height/= 100
    bmi=round((weight/(height*height)))
    if bmi > 18.5:
        return "저체중"
    elif bmi >= 18.5 and bmi<23:
        return "보통"
    elif bmi >= 23 and bmi<25:
        return "과체중"
    elif bmi > 25:
        return "비만"

bmi=get_bmi(176,69)
print(bmi)

print('================================')

def get_bmi(height, weight):
    height /=100
    bmi = weight / height**2
    return round(bmi, 1)

bmi = get_bmi(176, 69)
print(bmi)

if bmi <18.5:
    print('저체중')
elif 18.5 <= bmi < 23:
    print('정상')
elif 23 <= bmi <25:
    print('과체중')
elif 25 <= bmi:
    print('비만')


# 핸드폰 번호를 입력할 때 - 있든, 없든 없이 출력하기
phone_number1 = "010-2540-5357"
phone_number2 = "010 7584 1367"
phone_number3 = "01073201685"
phone_number = phone_number1
result = phone_number1.replace('-', '').replace(' ', '')
print(result)
result = phone_number2.replace(' ', '')
print(result)
print('\n')
print('=================================\n')

# 구구단 7단 출력하기
# i: 1~9
for dan in range(2, 9 + 1):
    for i in range(1,10):
        print(f'{dan} x {i} = {dan*i}')
    print()

print('=====================================\n')
# 2단부터 7단까지 출력하기 break
for dan in range(2, 9 + 1):
    for i in range(1,10):
        print(f'{dan} x {i} = {dan*i}')
    print()
    if dan == 7:
        break

# 구구단 2~7단 출력하되, x1, x3, x5, x7, x9 인것만 출력하기
for dan in range(2, 10):
    for i in range(1,10):
        if i % 2 == 0: #i == 2  or i == 4 or i == 6 or  i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print()
    if dan == 7:
        break

# 2단부터 7단 출력하되, x1,x3,x5,x7 x9 인것만 출력
for dan in range(2, 9 + 1): #2~9
    for i in range(1, 9 + 1): #x1~x9
        # if i == 2 or i == 6 or i == 8 :
        if i % 2 == 0:
            continue
        print(f"{dan} x {i} = {dan * i}")
    print()
    if dan == 7:
        break
'''

'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''
'''
def n_sum(number):
    sum =
result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1
'''
def n_sum(n):
    new = str(n)
    add = 0
    if n >= 1000000000:
        return -1
    for i in range(len(new)):   #'408' 3 range(3): i -> 0, 1, 2
        add += int(new[i])      #new[0] = '4'
    return add

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1

print('----------------------------------\n')

'''
Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''
# def get_subway_fare(km):
#     import math
#     fee = 720
#     price = 0;
#     if km < 10:
#         return fee
#     elif 10 <= km < 50:
#         price = math.ceil((km-10)/5 * 100 + fee)
#         return price
#     elif 50 < km:
#         price = (km -10)/8 * 100 + fee
#         return price
#
# get_subway_fare(26)
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

import math
def get_subway_fare(km):
    if km < 10:
        return 720
    elif 10 <= km < 50:
        fare = math.ceil((km-10)/5)
        result = fare * 100 + 720
        return result
    else:
        fare = 720 + (50-10)//5 * 100
        add = math.ceil((km-50)/8)
        result = fare+(add*100)
        return result

fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(25)
print(fare)        #1020
fare = get_subway_fare(61)
print(fare)        #1720

print('----------------------------------\n')

'''
Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''
# def get_three_six_nine(i):
#         str_i = str(i)
#         count_369 = 0
#         for x in str_i:
#             if (x == '3') or (x == '6') or (x == '9'):
#                 count_369 += 1
#         if count_369 == 0:
#             print(i)
#         else:
#             print(count_369 * '짝')
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝


'''
Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
1. 함수의 이름을 정해준다.
2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
3. 리턴하는 것을 말해준다.
4. 출력 예시를 보여준다.
5. 내가 낸 문제의 답안을 제출한다.
'''
'''
check_win이라는 함수를 만든다. 이 함수에 사용자와 컴퓨터를 넣고 사용자가 가위 바위 보 중 하나를 
입력해서 컴퓨터와 게임을 할 수 있게 한다. 
'''
# from random import randint
#
# rock_scissor_paper = {0: '가위', 1: '바위', 2: '보', 3: '가위', 4: '바위'}
# user = input("가위, 바위, 보 중 하나를 입력 :")
#
# def check_win(user, computer):
#     if user < computer:
#         return '이겼습니다'
#     elif user > computer:
#         return "졌습니다"
#     else:
#         return "비겼습니다"
#
# if user == '가위':
#     computer = randint(2, 4)
#     print(check_win(3, computer))
# elif user == '바위':
#     computer = randint(0, 2)
#     print(check_win(1, computer))
# else:
#     computer = randint(1, 3)
#     print(check_win(2, computer))

'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return "소수 아님"
        return "소수"

result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
def get_compliment(text):
    if "고구마" in text:
        return "왓쇼이"
    elif "맛있는" in text:
        return "우마이"
    elif "놀랄 만한" in text:
        return "요모야..!"
    elif "황당한" in text:
        return "요모야..!"
    elif "굉장한" in text:
        return "요모야..!"
    else:
        return "으무!"

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!

# ============================================================================================
# Quiz5-1. 모듈이란?
# 필요한 것들 끼리 부품처럼 잘 만들어진 파일

# Quiz5-2. 패키지란?
# 모듈들을 모아놓은 집합

# Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
# from theater_mudule import price_soldier as price

# Quiz5-4. __all__의 역할은?
# import 할 수 있는 모듈 정의함

# Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
# if __name__

# Quiz5-6. travel_temp 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
# import travel_temp.vietnam
# <가>
# from travel_temp import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel_temp import vietnam
# < 나 >
# from travel_temp import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel_temp.vietnam import ThailandPackage
# < 다 >
# from travel_temp.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()











