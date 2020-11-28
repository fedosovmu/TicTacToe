from GameState import *
from Player import *

class TicTacToeGame:
    def __init__(self):
        self.game_state = GameState()
        self.player_X = Player('player X')
        self.player_O =  Player('player O')

    def print_board(self):
        board = self.game_state.board
        board_for_print = """\
==Game==={:02d}==
| {} | {} | {} |
| {} | {} | {} |
| {} | {} | {} |
=============""".format(
            self.game_state.move_number,
            board[0], board[1], board[2],
            board[3], board[4], board[5],
            board[6], board[7], board[8],
        )
        print(board_for_print)

    def start(self):
        self.game_state._build_game_states_three()
        self.print_board()
        is_game_finish = False

        while not is_game_finish:
            if self.game_state.current_player == 'X':
                move = self.player_X.make_move()
            else:
                move, best_result = self.game_state.get_best_move()           
            self.game_state.make_move(move)
            is_game_finish = self.game_state.is_game_finish()
            self.print_board()

        winner = self.game_state.get_winner()
        print('Игра окончена. Победил {}'.format(winner))   