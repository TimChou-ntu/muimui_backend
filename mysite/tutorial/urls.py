from django.urls import path, re_path

from .views import EchoView, CarView, ClientView, CarDetailView

urlpatterns = [
    # path('', index, name='index'),
    re_path(r'^tutorial/?$', EchoView.as_view()),
    re_path(r'^cars/?$', CarView.as_view()),
    re_path(r'^cars/(?P<token_id>\w+)/', CarDetailView.as_view()),
    re_path(r'^clients/?$', ClientView.as_view()),
]
