import json
from django.db import models


class Board(models.Model):
    """
    A board object is a representation of a Connect Four game.
    It's stored on a JSON field that for simplicity will be a TextField in this case.

    Board representation, is stored on state field. That field has a dictionary
    the keys of the dictionary are columns, in the value we store the each row for the given
    column. See example of an empy board:

    state = {
        1: [0, 0, 0, 0, 0, 0]
        2: [0, 0, 0, 0, 0, 0]
        3: [0, 0, 0, 0, 0, 0]
        5: [0, 0, 0, 0, 0, 0]
        6: [0, 0, 0, 0, 0, 0]
        7: [0, 0, 0, 0, 0, 0]
    }

    """
    COLS = 7
    ROWS = 6
    PLAYER1 = 1
    PLAYER2 = 2
    EMPTY = 0

    created = models.DateTimeField(auto_now_add=True, editable=False)
    state = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'{}'.format(self.created)

    def __str__(self):
        return '{}'.format(self.created)

    def new_game(self):
        state = {}
        for col in range(1, self.COLS + 1):
            state[col] = [self.EMPTY for row in range(1, self.ROWS + 1)]
        self.set_board(state)

    def get_board(self):
        return json.loads(self.state)

    def set_board(self, board):
        self.state = json.dumps(board)
        self.save()

    def play(self, player_number, column_number):
        """
        Given a player and column.
        It will add the player piece on the position.
        Returns True if possible, False if there's not more space
        """
        board = self.get_board()
        rows = board[str(column_number)]

        for i, row in enumerate(rows):
            # if current row is not empty, then we have no more space
            if row != self.EMPTY:
                return False
            # if we hit the bottom place the piece
            if i == self.ROWS - 1:
                rows[i] = player_number
                self.set_board(board)
                return True
            # if next piece is not empty place the piece here
            elif rows[i + 1] != self.EMPTY:
                rows[i] = player_number
                self.set_board(board)
                return True
        return False

    def check_winner(self):
        """
        Returns PLAYER1, PLAYER2 if there's a winner on the current state of the game
        None for no winner
        """
        # TODO: implement functionality
        return None
