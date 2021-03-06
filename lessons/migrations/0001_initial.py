# Generated by Django 4.0.dev20210315091521 on 2021-03-19 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Data publikacji')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=200)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
        ),
    ]
