from copy import copy


class GameState:
    def __init__(self, game_state = None, move = None):
        if game_state is not None:
            self.move_number = game_state.move_number
            self.current_player = copy(game_state.current_player)
            self.board = copy(game_state.board)
        else:
            self.move_number = 1
            self.current_player = 'X'
            self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self._moves_three = {}
        if move is not None:
            self.make_move(move)

    def __repr__(self):
        repr_str = "[{}] {}".format(','.join(self.board), self.winner)
        return repr_str

    def make_move(self, move):     
        if self.board[move] != ' ':
            raise Exception('Position taken')

        self.board[move] = self.current_player

        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        self.move_number += 1

    def get_winner(self):
        if self.move_number > 9:
            return ' '

        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in winning_combinations:
            first = self.board[combination[0]]
            second = self.board[combination[1]]
            third = self.board[combination[2]]

            if first == second and first == third and (first == 'X' or first == 'O'):
                return first     
        return None    

    def is_game_finish(self):
        winner = self.get_winner()
        return winner is not None

    def get_available_moves(self):
        available_moves = []
        for i in range(len(self.board)):
            if self.board[i] == ' ':
                available_moves.append(i)
        return available_moves

    def get_best_move(self):
        if self.is_game_finish():
            return None
        available_moves = self.get_available_moves()
        if len(available_moves) == 0:
            return None

        if self.current_player == 'X':
            game_result_priority = {'O': 0, ' ': 1, 'X': 2}
        else:
            game_result_priority = {'X': 0, ' ': 1, 'O': 2}

        best_result = 0
        best_move = 0
        for move, game_state in self._game_states_three.items():
            winner = game_state.get_winner()
            if winner is not None:
                game_result = game_result_priority[winner]
                if game_result > best_result:
                    best_result = game_result
                    best_move = move
            else:
                (gs_best_move, gs_best_result) = game_state.get_best_move()
                if gs_best_result > best_result:
                    best_result = gs_best_result
                    best_move = move
        return (best_move, best_result)
        
    def _build_game_states_three(self):
        print('Start build', self.board)
        self._game_states_three = {}
        if not self.is_game_finish():
            available_moves = self.get_available_moves()
            for move in available_moves:
                new_game_state = GameState(self, move)
                if new_game_state.is_game_finish():
                    new_game_state._build_game_states_three()
                self._game_states_three[str(move)] = new_game_state