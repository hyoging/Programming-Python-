class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)  # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'
    def show_board(self):
        print(self.board)
    def set(self, row, col):
        pass
    def set_winner(self):
        # 클링2김1박1
        # -3줄
        # | 3줄

        # 포피포피
        # /
        # \
        # 무승부: 위의 조건 통과

        pass

    def change_trun(self):
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()
    game_engine.set(2, 2)
    game_engine.show_board()
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()
    game_engine.change_trun()
    print(game_engine.turn)
    game_engine.change_trun()
    print(game_engine.turn)