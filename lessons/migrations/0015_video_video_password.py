# Generated by Django 4.0.dev20210315091521 on 2021-03-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_alter_lesson_id_alter_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]