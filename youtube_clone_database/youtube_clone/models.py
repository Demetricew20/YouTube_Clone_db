from django.db import models

class Video(models.Model):
    yt_video_id = models.CharField(max_length=11, primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    dislikes = models.IntegerField(default=0, null=True, blank=True)




