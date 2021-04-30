from django.db import models

# Create your models here.
class Comment(models.Model):
    video = models.ForeignKey('youtube_clone.Video', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=120, blank=True)
    original_comment = models.ForeignKey('comments.Comment', blank=True, null=True, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField( default=False)
