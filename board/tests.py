from django.test import TestCase
from .models import Board


class BoardModelTest(TestCase):

    def test_new_game(self):
        # GIVEN a board object
        self.board = Board.objects.create()

        # WHEN a new game is call
        self.board.new_game()

        # THEN the board is correctly set
        board = self.board.get_board()
        self.assertEqual(len(board.keys()), Board.COLS,
                         'Check the number of cols in a new game is correct')
        self.assertEqual(len(board['1']), Board.ROWS,
                         'Check the number of rows in a col')

    def test_play(self):
        # GIVEN a new game on a board object
        self.board = Board.objects.create()
        self.board.new_game()

        # WHEN a play of player 1 in col 1 is call
        self.board.play(Board.PLAYER1, 1)

        # THEN the piece of the player is at the bottom of the row
        board = self.board.get_board()
        self.assertEqual(board['1'][Board.ROWS - 1], Board.PLAYER1,
                         'The piece of the player 1 is at the bottom')
