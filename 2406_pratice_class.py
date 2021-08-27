class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()




# ---------------------------------------------------------------------------------------------------
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화를 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군이이 영화 보러 갔을 때

# import  theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)
#
# from theater_module import price, price_morning
# price(5)
# price_morning(6)

from theater_module import price_soldier as price
price(5)






