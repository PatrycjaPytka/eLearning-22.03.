# Generated by Django 4.0.dev20210315091521 on 2021-03-26 12:08

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_aboutus_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='telephone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
