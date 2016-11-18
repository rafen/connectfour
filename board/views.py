from collections import OrderedDict
from django.views.generic import TemplateView
from .models import Board


class BoardView(TemplateView):
    template_name = "board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['player_number'] = kwargs['user_pk']
        # get Board, for simplicity we get or create one
        board, created = Board.objects.get_or_create()
        if not board.state:
            board.new_game()
        # sort dictionary by col to simplify rendering
        context['board'] = OrderedDict(sorted(board.get_board().items(), key=lambda t: t[0]))
        # render helpers for table
        context['rows'] = range(board.ROWS)
        return context
