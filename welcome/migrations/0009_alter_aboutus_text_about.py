# Generated by Django 4.0.dev20210315091521 on 2021-03-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_remove_contactus_telephone_contactus_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='text_about',
            field=models.CharField(max_length=1000),
        ),
    ]
