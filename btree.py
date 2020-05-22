from btnode import BTNode
import random
from copy import deepcopy


class BTree:
    """ Tree with random move chooser """

    def __init__(self, board=None):
        self.node = BTNode(board)

    def ai_turn(self, current, comp):
        """
        :param current: player sign
        :param comp: ai character 'x' or 'o'
        """

        def recursion(node, rec):
            """
            :param node: current tree node
            :param rec: depth pointer
            """
            # if end of the loop
            if node is None:
                return -100000, None
            # check for winner
            last = node.board.get_end()
            if last == current:
                return 1, None
            elif last == 'draw':
                return 0, None
            elif last == comp:
                return -1, None

            player = comp
            if rec % 2 == 0:
                player = current

            moves = node.board.free_moves()
            r = ()
            l = ()

            if len(moves) > 0:
                l = random.choice(moves)
                moves.remove(l)
                board = deepcopy(node.board)
                board.move(l, player)
                node.left = BTNode(board)

            if len(moves) > 0:
                r = random.choice(moves)
                moves.remove(r)
                board = deepcopy(node.board)
                board.move(r, player)
                node.right = BTNode(board)

            l_pos = recursion(node.left, rec + 1)[0]
            r_pos = recursion(node.right, rec + 1)[0]

            if r_pos > l_pos:
                return r_pos + l_pos, r
            return r_pos + l_pos, l

        return recursion(self.node, rec=0)
