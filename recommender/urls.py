from django.urls import path
from recommender import views

urlpatterns = [
    path('', views.index, name="index"),
    path('result/<id>', views.result, name="result"),
    path('movie/', views.movie, name="movie"),
    path('tag/', views.tag, name="tag"),
    path('rank/', views.rank, name="rank"),
]