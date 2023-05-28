import random
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Song
from .models import Playlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        songs = Song.objects.filter(song_title__icontains=q)
    else:
        songs = Song.objects.all()
    lensongs = len(songs)
    context = {'songs':songs, 'lensongs': lensongs}
    return render(request, 'index.html', context=context)
                
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('index')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    

def myplaylists(request):
    songs = Song.objects.filter(playlist__user=request.user).distinct()
    lensongs = len(songs)
    if request.method == "POST":
        if 'Shuffle' in request.POST:
            songlist = list(songs)
            songs = random.sample(songlist, lensongs)
        elif request.POST:
            print(list(request.POST.keys()))
            song_id = list(request.POST.keys())[1]
            playlist_song = Playlist.objects.filter(song__id=song_id, user=request.user)
            playlist_song.delete()
            songs = Song.objects.filter(playlist__user=request.user).distinct()
            messages.info(request, "Song removed from playlist!")
    context = {'songs': songs, 'lensongs': lensongs}
    return render(request, 'myplaylists.html', context=context)

def songinfo(request, id):
    songs = Song.objects.filter(id=id)
    status = "Add To Playlist"
    song = Song.objects.get(id=id)
    if request.method == "POST":
        song = Song.objects.get(id=id)
        print(song)
        data = Playlist(song=song,user=request.user)
        data.save()
        messages.success(request, "Song added to playlist!")
        status = "My Playlist"
    context = {'songs': songs, 'status': status}
    return render(request, 'songinfo.html', context=context)

def album(request, album_name):
    songs = Song.objects.filter(album_name=album_name)
    print(songs)
    context = {'songs': songs, 'album_name': album_name}
    return render(request, 'album.html', context=context)



