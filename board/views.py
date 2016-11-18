from collections import OrderedDict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Board


class BoardView(TemplateView):
    template_name = "board.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BoardView, self).dispatch(*args, **kwargs)

    def _get_board(self):
        board, created = Board.objects.get_or_create()
        if not board.state:
            board.new_game()
        return board

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['player_number'] = kwargs['user_pk']
        context['message'] = kwargs.get('message', '')
        # get Board, for simplicity we get or create one
        board = self._get_board()
        # sort dictionary by col to simplify rendering
        context['board'] = OrderedDict(sorted(board.get_board().items(), key=lambda t: t[0]))
        # render helpers for table
        context['rows'] = range(board.ROWS)
        return context

    def post(self, request, *args, **kwargs):
        # TODO: Use a form to validate User input
        if 'new' in request.POST:
            self._new_game(request)
        else:
            kwargs['message'] = self._play(request)
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def _new_game(self, request):
        board = self._get_board()
        board.new_game()

    def _play(self, request):
        msg = ''
        res = False
        try:
            board = self._get_board()
            res = board.play(request.POST.get('player_number'), request.POST.get('column_number'))
        except Exception as e:
            msg = u'Error: {}'.format(e)
            res = False
        if not res:
            msg = u'Invalid play {}'.format(msg)
        return msg
