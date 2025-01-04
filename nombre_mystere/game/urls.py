from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_difficulty, name='select_difficulty'),
    path('game/', views.play_game, name='play_game'),
]
