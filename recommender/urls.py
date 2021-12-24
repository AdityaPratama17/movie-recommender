from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recommender/', views.recommender, name="recommender"),
    path('recommender/result/<id>', views.result, name="result"),
    path('user/', views.user, name="user"),
    path('movie/', views.movie, name="movie"),
    path('link/', views.link, name="link"),
]