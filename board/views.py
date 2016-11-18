from django.views.generic import TemplateView


class BoardView(TemplateView):
    template_name = "board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['player_number'] = kwargs['user_pk']
        return context
