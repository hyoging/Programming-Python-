from baseball_game_engine import make_answer, check
from custom_error import InvalidLengthErrork

answer = make_answer()

while True:
    guess = input("뭘까?")
    # 숫자인지 아닌지
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer)
        raise InvalidLengthExrror('정답의 길이와 다른 것을 입력했네요')

    strike, ball = check(guess, answer)
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
    if answer == guess:
        print("정답입니다.")
        break