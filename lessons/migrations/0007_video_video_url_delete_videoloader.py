# Generated by Django 4.0.dev20210315091521 on 2021-03-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_remove_video_video_url_videoloader'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='VideoLoader',
        ),
    ]