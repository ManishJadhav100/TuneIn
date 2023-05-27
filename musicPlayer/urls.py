from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #Playlist
    path('my-playlists/', views.myplaylists, name='myplaylists'),
    path('<int:id>/', views.songinfo, name='songinfo'),
    path('album/<str:album_name>', views.album, name='album')
]