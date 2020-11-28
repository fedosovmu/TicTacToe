class Player:
    def __init__(self, name):
        if name is not None:
            self.name = name
        else:
            self.name = 'player'

    def make_move(self):
        print('Ходит {}: '.format(self.name), end = '')
        move = int(input())
        return move