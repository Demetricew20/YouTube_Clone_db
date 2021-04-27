from django.db import models

# Create your models here.
class Comments(models.Model):
    video = models.ForeignKey('youtube_clone.Video', default=0, on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)
    comment_reply = models.ForeignKey('comments.Comments', max_length=120, default=None, blank=True, on_delete=models.CASCADE)
    like = models.BooleanField(default=None, null=True, blank=True)
    dislike = models.BooleanField( default=None, null=True, blank=True)