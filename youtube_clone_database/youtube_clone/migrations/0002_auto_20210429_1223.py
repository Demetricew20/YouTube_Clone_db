# Generated by Django 3.1.7 on 2021-04-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='yt_video_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]