# Generated by Django 3.1.7 on 2021-04-27 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0004_auto_20210426_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='yt_video',
            new_name='yt_video_id',
        ),
    ]
