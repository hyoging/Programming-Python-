import pickle

from person import Person

# 객체 생성하자
번호02 = Person('지창민', '하늘색')
번호06 = Person('김효진', '민트색')

# 리스트 만들자
절친 = [번호02, 번호06]
# print(절친)
# for 친구 in 절친:
#     print(친구)
# 저장하자
# 1.객체 하나 저장
with open('object.bin', 'wb') as f:
    pickle.dump(번호02, f)


# 2.객체 여러 개 저장
with open('objects.bin', 'wb') as f:
    pickle.dump(절친, f)