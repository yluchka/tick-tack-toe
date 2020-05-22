from btree import BTree
from board import Board


class Game:
    """Class to initialize and perform Tic Tac Toe game"""

    def __init__(self):
        """ Init game session """
        self.board = Board()
        # current player if not chosen
        self.player = 'o'
        # current opponent character if not chosen
        self.comp = 'x'

    def ask_side(self):
        """ Choose 'o' or 'x' """
        player = input('Do you wanna play first("x" or "yes")? ').strip().lower()
        if player in ['x', 'yes', 'y', 'yup', 'ye', 'yeah', 'ofc', 'of course']:
            self.player = 'x'
            self.comp = 'o'

    def end(self):
        """ Check if game is over """

        end = self.board.get_end()
        if end == self.player:
            return 'WIN!!!'
        elif end == 'draw':
            return 'Draw, nice'
        elif end == self.comp:
            return 'FAILED!!!'

    def move(self):
        """ Ask user move from input """
        pos = input('Your turn %s: ' % self.player.upper()).strip()
        while pos not in self.board.free_moves():
            print('These is representation of moves:')
            print('7 8 9\n4 5 6\n1 2 3')
            pos = input('Please, enter number from range [1-9]: ').strip()

        self.board.move(pos, self.player)

    def opponent_move(self):
        """ Computer turn """
        tree = BTree(self.board)
        self.board.move(tree.ai_turn(self.player, self.comp)[1], self.comp)


if __name__ == '__main__':
    # init
    game = Game()
    # ask 'x' or 'o' side from user
    game.ask_side()

    # while game is not over
    while not game.end():
        if game.player == 'o':
            game.opponent_move()
            print('------')
            print(game.board)

            if game.end():
                break

            game.move()

        else:
            print('------')
            print(game.board)
            game.move()
            if game.end():
                break
            game.opponent_move()

    print('\n-----')
    print(game.board)
    print(game.end())
