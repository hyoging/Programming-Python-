# 정답 만들자: 0~9 숫자 세개 뽑자
def make_answer():
    pass

def check(guess, answer):
    strike = 0
    ball = 0
    return strike, ball

if __name__ == '__main__':
    answer = make_answer()
    print(answer)
    strike, ball = check("832", "934")
    print(strike, ball)
    strike, ball = check("431", "934")
    print(strike, ball)
answer = make_answer()
# 무한반복
while True:
# 숫자 묻자
    guess = input("뭘까요~?")
# strike, ball 판정하자
    strike, ball = check(guess, answer)
# 출력하자
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
# 정답 == 숫자, 끝내자
    if answer == guess:
        print('정답입니다.')
        break