# Generated by Django 4.1.3 on 2022-11-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movie_meta_rating_movie_rott_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='summary',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_desription',
            field=models.TextField(default=''),
        ),
    ]
