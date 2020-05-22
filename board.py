import random


class Board:
    """ A class to represent a board in console for tic tac toe game """

    def __init__(self, board=None, positions=None):
        """
        :param board:
        :param positions:
        """
        if board:
            self.board = board
        else:
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
        if positions:
            self.positions = positions
        else:
            self.positions = {
                '7': (0, 0), '8': (0, 1), '9': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '1': (2, 0), '2': (2, 1), '3': (2, 2)}

    def __str__(self):
        x = ''
        for row in self.board:
            # redraw all elements
            for el in row:
                if el == ' ':
                    x += '🔳'
                elif el == 'o':
                    x += '⭕'
                elif el == 'x':
                    x += random.choice('✖')
            x += '\n'
        # remove last n
        return x[:-1]

    def __repr__(self):
        """ Print multiple boards at once"""
        return str(self)

    def get_end(self):
        """ Return winner of hte game if exists, else False """

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ' or \
                self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[1][1]

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
            elif self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False

        return "draw"

    def free_moves(self):
        """ Return free cell's numbers from 1 to 9 """
        res = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    res.append(str(3 * (2 - row) + 1 + col))

        return res

    def move(self, pos, char):
        """
        :param pos: number 1-9 position of current move
        :param char: sign of the character (comp or player)
        """
        if pos in self.positions:
            row, col = self.positions[str(pos)][0], self.positions[str(pos)][1]

            if self.board[row][col] == ' ':
                self.board[row][col] = char
                return True
        return False
