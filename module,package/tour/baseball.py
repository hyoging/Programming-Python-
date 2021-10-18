from baseball_game_engine import make_answer, check
from custom_error import InvalidLengthError

def save_history(answer, count, name):
    with open('baseball_history.txt', 'w', encoding='utf-8') as f:
        f.write(f'{answer}:{count}:{name}\n')
def load_history():
    count_name = {}
    with open('baseball_history.txt', 'r', encoding='utf=8') as f:
        print('-------history---------')
        while True:
            line = f.readline()
            if line == '':
                break
            print(line.rstrip())
            line = line.rstrip()
            data = line.split(':')
            count_name[data[1]] = data[2]    #{3: 'name'}
        count_name = sorted(count_name.items())
        return count_name[:3]

answer = make_answer()
count = 0
while True:
    guess = input("뭘까?(t: history, top3)")
    #t를 입력하면, 불러오자, top3
    if guess == 't':
        top3 = load_history()
        print(top3)
    # 숫자인지 아닌지
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):
        raise InvalidLengthError('정답의 길이와 다른 것을 입력했네요')
        print(f'정답의 길이와 다른 것을 입력했네요.{len(answer)}문자')
        continue
    strike, ball = check(guess, answer)
    count += 1
    print(f'{guess}\tstrike: {strike}, ball: {ball}\t+{count}try')
    if answer == guess:
        print("정답입니다.")
        #저장하자, 정답, 시도횟수
        name = input('이름은: ')
        save_history(answer, count, name)
        #불러오자, top3
        top3 = load_history()
        print(top3)
        break