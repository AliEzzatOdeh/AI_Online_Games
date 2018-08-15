from django.urls import path
from . import views

urlpatterns = [
    path('tic_tac_toe_game', views.index, name='tic_tac_toe_game')
]