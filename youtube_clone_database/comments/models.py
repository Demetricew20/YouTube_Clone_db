from django.db import models

# Create your models here.
class Comments(models.Model):
    video_id = models.ForeignKey('youtube_clone.Video', default=0, on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)
    like = models.BooleanField(default=None, null=True, blank=True)
    dislike = models.BooleanField( default=None, null=True, blank=True)