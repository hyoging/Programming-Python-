from baseball_game_engine import make_answer, check
from random import random
# 정답 만들자: 0~9 숫자 세개 뽑자
def make_answer():
    list_r = random.sample(range(9+1),3)
    return "".join(str, list_r)

def check(guess, answer):
    strike = 0
    ball = 0

    # 숫자 하나 꺼내서 정답에 있고, 자리가 같으면, strike += 1
    # 숫자 하나 꺼내서 정답에 있고, 자리가 다르면, ball += 1
    guess[0] in answer
