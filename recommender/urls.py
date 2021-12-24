from django.urls import path
from recommender import views

urlpatterns = [
    # rekomendasi
    path('', views.recommender_index, name="recommender_index"),
    path('genre-favorit/<int:id>', views.genre_favorit, name='genre-favorit'),
    path('rekomendasi-user-baru',views.rekomendasi_user_baru, name='rekomendasi-user-baru'),
    path('rekomendasi-0/<int:id>', views.rekomendasi_0, name='rekomendasi-0'),
    path('rekomendasi-1/<int:id>', views.rekomendasi_1, name='rekomendasi-1'),
    path('rekomendasi-2/<int:id>', views.rekomendasi_2, name='rekomendasi-2'),
    path('tambah-user', views.tambah_user, name='tambah-user'),
    path('ubah-user', views.ubah_user, name='ubah-user'),
    path('hapus-user', views.hapus_user, name='hapus-user'),

    # movie
    path('movie/', views.movie, name="movie"),
    path('tambah-movie', views.tambah_movie, name='tambah-movie'),
    path('ubah-movie', views.ubah_movie, name='ubah-movie'),
    path('hapus-movie', views.hapus_movie, name='hapus-movie'),


    path('tag/', views.tag, name="tag"),
    path('rank/', views.rank, name="rank"),
]