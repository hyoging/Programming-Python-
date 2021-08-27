class Hairshop:
    _HAIRSTYLE = ('컷트  10000', '매직  20000', '파마  30000', '염색  40000')
    _PRICE = ['10000', '20000', '30000', '40000']
    _HAIRSHOP = ('미림미용실', '수돌미용실', '효잔미용실', '4반미용실')
    _TIME = ('10:00', '12:00', '14:00', '16:00', '18:00', '20:00')

    def __init__(self):
        self.style = 0
        self.price = 0
        self.shop = 0
        self.time = 0
        self.name = ''
        self.select_designer = ''
        self.my_style = ''
        self.my_time = ''

    def set_name(self):
        name = input('이름을 입력하세요: ')
        self.name = '입력된 정보가 없습니다' if name == '' else name

    def set_shop(self):
        for index, shop in enumerate(Hairshop._HAIRSHOP):
            print(index+1, shop)
        shop = input('원하는 미용실을 선택하세요: ')
        self.shop = int(shop)

    def set_style(self):
        for index, style in enumerate(self._HAIRSTYLE):  # 스타일 종류 보여주자
            print(index + 1, style)
        style = input('원하는 헤어스타일을 선택하세요: ')
        self.style = self._HAIRSTYLE[int(style) - 1]
        self.price = self._PRICE[int(style) - 1]

    def set_designer(self):
        select_designer = input('원하는 디자이너를 입력하세요: ')
        self.select_designer = '입력된 정보가 없습니다' if select_designer == '' else select_designer

    def set_mystyle(self):
        my_style = input('현재 자신의 헤어스타일을 입력하세요: ')
        self.my_style = '입력된 정보가 없습니다' if my_style == '' else my_style

    def set_time(self):
        for index, time in enumerate(Hairshop._TIME):
            print(index+1, time)
        time = input('원하는 예약시간대를 선택하세요: ')
        self.time = int(time)

    def __str__(self):
        return '-' * 10 + '예약확인' + '-' * 10 + f'\n이름: {self.name}\n미용실: {Hairshop._HAIRSHOP[self.shop-1]}\n디자이너: {self.select_designer}\n' \
                                              f'자신의 헤어스타일: {self.my_style}\n원하는 헤어스타일: {self.style}' \
                                              f'\n가격:  {self.price}\n예약시간: {Hairshop._TIME[self.time-1]}\n' + '-' * 26

    def set_hair_shop(self):
        self.set_name()
        self.set_shop()
        self.set_designer()
        self.set_mystyle()
        self.set_style()
        self.set_time()
        print(self.__str__())