from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.song_title
    
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song, self.user

