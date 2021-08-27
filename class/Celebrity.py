class Celebrity:
    def __init__(self, name):
        #이름
        self.name = name
        #소속사
        #group

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    def __str__(self):
        return f'이름: {self.name}\t소속사 : {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)           #Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마 : {self.drama}\t소속사 : {self.entertainment}'
        # return f'이름: {self.name}\t소속사 : {self.entertainment}'

class Singer(Celebrity):
    def __init__(self,name, song):
        super().__init__(name)
        self.song = song


    def __str__(self):
        return super().__str__() + f'\t노래 : {self.song}'

현진 = Singer('현진', '신메뉴')
현진.set_entertainment('JYP')
print(현진)
필릭스 = Singer('필릭스', 'BackDoor')
필릭스.set_entertainment('JYP')
print(필릭스)

스트레이키즈 =[]
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)

for 멤버 in 스트레이키즈:
    print(멤버)
# for i in range(len(스트레이키즈)):
#     print(스트레이키즈[i])

Q = Celebrity('지창민')
# Q.set_name('지창민')
Q.set_entertainment('cre.ker')
# Q.info()
# print(Q.name, Q.entertainment)
print(Q)

영훈 = Celebrity('김영훈')
# Q.set_name('지창민')
영훈.set_entertainment('cre.ker')
# Q.info()
# print(Q.name, Q.entertainment)
print(영훈)

박보검 = Talent('박보검')
박보검.set_entertainment('blossom')
박보검.set_drama('응답하라 1988')
print(박보검)