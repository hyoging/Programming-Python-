class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)  # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'
    def show_board(self):
        print('  '.join(self.board[0:3]))
        print('  '.join(self.board[3:6]))
        print('  '.join(self.board[6:9]))

        for i, v in enumerate.self.board:
            print(v + '  ', end='')
            if i % 3 == 2:
                print()

    def set(self, row, col):
        self.board[(row*3-3) + (col-1)] = self.turn
        index = (row - 1) * 3 + (col - 1)
        self.board[index] = self.turn

    def set_winner(self):
        # 클링2김1박1
        # -3줄

        # if set.board[self.position_to_index(row ,1)]\
            #     ==set.board[self.position_to_index(row,2)]]\
            #     ==set.board[self.positon_to_index(row, 3)]\
            #     == self.turn:
            # return ''

        if self.borad[self.position_to_index(1, 3)]\
            ==self.borad[self.position_to_index(2,2)]\
            ==self.borad[self.position_to_index(3,3)]\
            ==self.turn:
            return '\\'

        if self.borad[2] == 'X' and self.borad[4] == 'X' and self.borad[6] == 'X':
            return print('X 승리')

        if self.borad[0] == 'X' and self.borad[4] == 'X' and self.borad[8] == 'X':
            return print('X 승리')

            # 끝나는 경우 : 무승부(승자가 없는 상태로 놓을 자리가 없음), 승자 결정(승자가 있음)
        if self.borad[0] != '.' and self.borad[1] != '.' and self.borad[2] != '.' and \
                self.borad[3] != '.' and self.borad[4] != '.' and self.borad[5] != '.' and \
                self.borad[6] != '.' and self.borad[7] != '.' and self.borad[8] != '.':
            return print('무승부')

        pass

    def change_trun(self):
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X':
        self.turn = 'O' if self.turn == 'X' else 'X'

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