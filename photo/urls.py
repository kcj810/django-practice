from django.urls import path
from photo import views
# from photo.models import Album, Photo

app_name = 'photo'
urlpatterns = [
    # Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # Example: /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # Example: /photo/album/99
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]

# views에 코딩하지 않고 urls에서 바로 구현하는 방법. MVT를 고려하면 사용하지 않는 편이 좋음

# app_name = 'photo'
# urlpatterns = [
#     # Example: /photo/
#     path('', views.AlbumLV.as_view(model=Album), name='index'),
#
#     # Example: /photo/album/, same as /photo/
#     path('album', views.AlbumLV.as_view(model=Album), name='album_list'),
#
#     # Example: /photo/album/99/
#     path('album/<int:pk>/', views.AlbumDV.as_view(model=Album), name='album_detail'),
#
#     # Example: /photo/album/99
#     path('photo/<int:pk>/', views.PhotoDV.as_view(model=Photo), name='photo_detail'),
# ]