# Generated by Django 4.0.dev20210315091521 on 2021-03-24 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_video_video_url_delete_videoloader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.CreateModel(
            name='VideoLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('video_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.video')),
            ],
        ),
    ]
