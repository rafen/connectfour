from django.conf.urls import url
from .views import BoardView


urlpatterns = [
    url(r'games/(?P<user_pk>[-\w]+)/$', BoardView.as_view(), name='board'),
]
