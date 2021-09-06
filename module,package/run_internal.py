# math
import math
print(math.ceil(3.5))
print(math.floor(3.5))    # floor : 바닥
print(math.pow(2, 10))
print(math.sin(math.pi/2))

# random
import random
print(random.random())            #java random : 0.0 <= r < 1.0
print(random.randrange(1, 10))      #1<=r < 10 정수
print(random.randint(1, 10))        #1<=r <=10 정수
list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1))         # liist1 중 하나

print('before : ', list1)
print(random.shuffle(list1))        #list1 섞기
print(list1)

print(random.sample(list1, 2))               #list1에서 랜덤으로 n개 뽑기

# datetime
import datetime
print('-'*20)
import  datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 7, 12)
print(birthday)
print(now - birthday)

# 1
# import math
# math.floor(62421)
# math.floor(59827)

import math
bill = 62421
bill = 59827
print(bill //100*100)
print(bill - bill%100)
print(math.floor(bill/100)*100)
print(int(bill/100)*100)

# 2
# import math
# math.round(93)
# math.round(56)

score = 56
print(round(score/10)*10)
print(round(score, -1))

# 3
# import random
# list = []
# ran_num = random.randint(1,45)
# for i in range(6):
#     while ran_num in list:
#         ran_num = ran_num.randint(1,45)
#     list.append(ran_num)
# list.sort()
# print(list)

import random
# 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?
print(random.sample(range(1, 45 + 1), 6))
list_r = random.sample(range(1, 9+1), 3)
print(list_r)
print("".join(str(n) for n in list_r))
print("".join(map(str, list_r)))

# 4
list2 = [1,2,3,4,5,6,7,8,9]
list3 = []
for i in range(3):
    number = random.choice(list2)
    list3.append(str(number))
    list2.remove(number)
print(list3[0] + list3[1] + list3[2])

# 5
# import  datetime
# now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.hour)
# birthday = datetime.datetime(2004, 7, 12)
# print(birthday)
# print(now - birthday)
import datetime
birthday = datetime.datetime(2004,7,12)
now = datetime.datetime.now()
print(now - birthday)

# 6
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.hour)
# christmas = datetime.datetime(2021,12,25)
# print(christmas)
# print(christmas - now)

christmas = datetime.datetime(2021, 12, 25)
print(christmas - now)

# 7
# import datetime
# now = datetime.datetime.now()
# mybirthday = datetime.datetime(2022,7,12)
# print(mybirthday)
# print(mybirthday - now)

# my_birthday = datetime.datetime(2021, 7, 12)
# if my_birthday < now:
#     my_birthday = my_birthday.replace(year=2022)
#     my_birthday.year = my_birthday.year+1
# print(my_birthday - now)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
last_number = input("마지막 번호는?")
# 마지막 번호 묻자
list_class = list(range(1, int(last_number) + 1))
print(list_class)
# 1 ~ 마지막번호까지 숫자 리스트 만들자
# 반복
while True:
# 뺄 번호 문자
    exclude_number = input("뺄 번호는?(enter치면 그만 빼기")
# 다 뺐으면 반복 끝내자
    if exclude_number =='':
        break
# 빼자
    list_class.remove(int(exclude_number))
    print(list_class)
# 섞자
    random.shuffle(list_class)
# 출력하자
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i}\t{number}')




