# Generated by Django 4.1.3 on 2022-11-15 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
    ]
