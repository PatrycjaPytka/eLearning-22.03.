# Generated by Django 4.0.dev20210315091521 on 2021-03-26 12:11

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_aboutus_email_aboutus_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('telephone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='email',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='telephone',
        ),
    ]
