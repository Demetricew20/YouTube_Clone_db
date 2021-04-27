# Generated by Django 3.1.7 on 2021-04-27 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('youtube_clone', '0003_remove_video_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=120)),
                ('like', models.BooleanField(blank=True, default=None, null=True)),
                ('dislike', models.BooleanField(blank=True, default=None, null=True)),
                ('video_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='youtube_clone.video')),
            ],
        ),
    ]
