from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('home/', views.home),
    path('words_list', views.wordlist),
    path('words_list/', views.wordlist),
    path('add_word', views.addword),
    path('add_word/', views.addword),
]