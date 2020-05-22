class BTNode:
    """ Node to represent a board with two daughter boards """

    def __init__(self, board=None):
        """
        :param board: Baord object
        """
        self.board = board
        self.right = None
        self.left = None
