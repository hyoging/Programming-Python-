# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
#
# print('풍선')
# print('나비')
# print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
# print("ㅋ"*9)
#
# # 참/거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))
#
# # 애완동물을 소개해 주세요~
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3
#
# print("우리집" + animal + "강아지의 이름은" + name + "예요")
# print(name + "는"+ str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))
#
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3
#
# print("우리집" + animal + "강아지의 이름은" + name + "예요")
# print(name + "는"+ str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))
#
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")
#
# print(1+1)      # 2
# print(3-2)      # 1
# print(5*2)      # 10
# print(6/3)      # 2
#
# print(2**3)     # 2^3 = 8
# print(5 % 3)      # 나머지 구하기 2
# print(10 % 3)     # 1
# print(5//3)     # 1
# print(10//3)    # 1
#
# print(10 > 3)      # True
# print(4 >= 7)   # False
# print(10 < 3)     # False
# print(5 <= 5)    # True
#
# print(3 == 3)      # True
# print(4 == 2)    # False
# print(3+4 == 7)    # True
#
# print(1 != 3)    # True
# print(not(1 != 3))    # False
#
# print((3>0) and (3 < 5))      # True
# print((3>0) & (3 < 5))        # True
#
# print((3>0) or (3 > 5))       # True
# print((3>0) | (3 > 5))        # True
#
# print(5>4>3)        # True
# print(5>4>7)        # False
#
# print(2+3*4)    # 14
# print((2+3)*4)  # 20
# number = 2+3*4  # 14
# print(number)
# number = number + 2     # 16
# print(number)
# number += 2     # 18
# print(number)
# number *= 2  # 36
# print(number)
# number /= 2    # 18
# print(number)
# number -= 2      # 16
#
# number %= 5
# print(number)
#
# print(abs(-5))    # 5
# print(pow(4, 2))    # 4^2 = 4*4 = 16
# print(max(5, 12))    # 12
# print(min(5, 12))   # 5
# print(round(3.14))   # 3
# print(round(4.99))   # 5
#
# from math import *
# print(floor(4.99))  # 내림.4
# print(ceil(3.14))   # 올림.4
# print(sqrt(16))     # 제곱근.4
#
# from random import *
#
# print(random())     # 0.0 ~1.0 미만의 임의의 값 생성
# print(random() * 10)    # 0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10))     # 0~10미만의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
#
# print(int(random() * 45) + 1)   # 1~45이하의 임의의 값 생성
#
# print(randrange(1, 46))     # 1~46 미만의 임의의 값 생성
#
#
# # Quiz
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월" + str(date) + " 일로 선정되었습니다")
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
#
# jumin = "990120-1234567"
#
# print("성별 :" + jumin[7])
# print("연 : " + jumin[0:2])  # 0부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
#
# print("생년월일 : " + jumin[:6])    # 처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:])   # 7부터 끝까지
# print("뒤 7자리(뒤에부터) : " + jumin[-7:])
# #  맨 뒤에서 7번째부터 끝까지
#
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper)
# print(len(python))
# print(python.replace("Python", "Java"))
#
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
#
# print(python.find("Java"))
# # print(python.index("Java"))
# print("hi")
#
# print(python.count("n"))

# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며,{color}색을 좋아해요.".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4(v3.6이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩'입니다.")

# \\ : 문장 내에서 \
# print("C:\python\venv\Scripts\python.exe C:/python/practice.py")

# \r : 커서를 맨 앞으로 이동
# print("C:\python\venv\Scripts\python.exe C:/python/practice.py")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스2 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

# Quiz
# url = "https://www.naver.com/"
# my_str = url.replace("http://", "")    # 규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")]     # 규칙2
# my_str(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트[]

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway 3 = 30

# subway = [10, 20, 30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
#
# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
#
# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
#
# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
#
# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)
#
# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
#
# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)
#
# # 모두 지우기
# num_list.clear()
# print(num_list)
#
# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)
#
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)
#
# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# 간 손님
# del cabinet["A-3"]
# print(cabinet)

# key 들만 출력
# print(cabinet.keys())

# value 들만 출력
# print(cabinet.values())

# key, value 쌍으로 출력
# print(cabinet.items())

# 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
#
# # menu.add("생선까스")
#
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
#
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)
#
# # 집합(set)
# # 중복안됨, 순서없음
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
#
# 교집합(java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
#
# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
#
# 차집합(java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
#
# python 을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#
# # java 를 잊었어요
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu =tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))

#Quiz
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
# users = range(1, 21)
# print(type(users))
# users = list(users)
# print(type(users))

# print(users)
# shuffle(users)
# print(users)
#
# winners = sample(users, 4)
#
# print("--당첨자 발표--")
# print("치킨 당첨자 : {0}".format())
# print("커피 당첨자 : {0}".format())
# print("--축하합니다--")


# print("---------------------------------------")
# if
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")
#
# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <= 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for
# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))
#
# starbucks = ["아이언맨" , "토르" , "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


 # while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0},커피가 준비 되었습니다. {1} 번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")
#
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1} 회".format(customer,index))
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue와 break
# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐.".format(student))

# students = [1,2,3,4,5]
# print(students)
# students = [1+100 for i in students]
# print(students)
# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [Ien(i) for i in students]
# print(students)
# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# quiz
# from random import *
# cnt = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[0] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0} 번째 손님(소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {0} 분".format(cnt))

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money
#
# balance = 0
# balance = deposit(balance ,1000)
# print(balance)
#
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은{0} 원입니다.".format(balance))
#
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
#
#
#     balance = 0
#     balance = deposit(balance, 1000)
#     # balance = withdraw(balance, 2000)
#     # balance = withdraw(balance, 500)
#     commission, balance = withdraw_night(balance, 500)
#     print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
#
# # 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name,age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
#
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name,age, main_lang))
#
# profile("유재석")
# profile("김태호")
#
# # 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="자바",age="25",name="김태호")
#
# # 가변인자
# # def profile(name, age, lang2, lang3, lang4, lang5):
# #     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
# #     print(lang1, lang2, lang3, lang4, lang5)
#
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20,"python", "Java","C","C++","C#")
# profile("김태호", 25,"kotlin", "Swift")
#
# # 지역변수와 전역변수
# gun =10
#
# def checkpoin(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return  gun
#
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
#
# # quiz
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height *height * 21
#
# height = 175
# gender = "남자"
# weight = std_weight(height /100, gender)
# print("키(cm) {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
import thailand

print("===============================")
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린" #유닛의 이름
hp = 40     #유닛의 체력
damage = 5  # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드/ 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 뱡향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시",tank_damage)
attack(tank2_name, "1시", tank2_damage)

print("===============================")

from random import *
# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        # self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(name))

    # def move(self, location):
    # print("[지상 유닛 이동]")
    # print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
    #           .format(self.name, location, self.speed))

    def damage(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
    # def move(self, location):
    #     print("[지상 유닛 이동]")
    #     print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
    #           .format(self.name, location, self.speed))
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.cloking = True
#
# if wraith2.cloking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 뱡향으로 적군을 공격 합니다. [공격력 {2}]")\
            .format(self.name, location, self.damage)

    # def damage(self, damage):
    #     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    #     self.hp -= damage
    #     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    #     if self.hp <= 0:
    #         print("{0} : 파괴되었습니다.".format(self.name))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40,1,5)

        # 스팀팩: 일정 시간동안 이동 및 공격 속도를 증가 ,체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 놓은 파워로 공격 가능. 이동 불가
    seize_developed = False   #시즈모든 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_size_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐때 -> 시즈모드
        if self.size_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode = False

# 메딕: 의무병
# 파이어뱃 : 공격, 유닛, 화염 방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attck("5시")

# 공격 2번 받는다고 가정
firebat1.damage(25)
firebat1.damage(25)

# 드랍쉽  : 공중 유닛, 수송기, 마린 / 파이어뱃/ 탱크 등을 수송. 공격X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [ 속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,0, damage)  #지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, location)
        super().__init__(name, hp, 0)
        self.location = location
        # pass

# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500 , "7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     pass
#
# game_start()
# game_over()






# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6,5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False   #클로킹 모드(해제상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드 -> 모드 해제
            print("{0}  클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else: #클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player : gg")
    print("[player]님이 게임ㅁ에서 퇴장하셨습니다.")

#게임 시작
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리(생성된 모든 유닛 apped)
attack_units = []
attack_units.apped(m1)
attack_units.apped(m2)
attack_units.apped(m3)
attack_units.apped(t1)
attack_units.apped(t2)
attack_units.apped(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱그 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(random(5,21))   #공격은 랜덤으로 받음(5~20)

#게임 종료
game_over()

#Quiz
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

        #매물 정보 표시
        def show_detail(self):
            print(self.location, self.house_type,self.deal_type\
                  ,self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트","매매", " 10억", "2010년")
house2 = House("마포", "오피스텔","전세", " 5억", "2007년")
house3 = House("송파", "빌라","월세", " 500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail


# --------------------------------------------------------------------------------
# import travel_temp.thailand
# trip_to = travel_temp.thailand.ThailandPackage()
# trip_to.detail()
#
# from travel_temp.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel_temp import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()



# from travel_temp import*
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))











