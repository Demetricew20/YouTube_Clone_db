from django.db import models

class Video(models.Model):
    comments = models.CharField(max_length=120, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
