# Generated by Django 4.1.3 on 2022-11-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='meta_rating',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='movie',
            name='rott_rating',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.FloatField(default=-1),
        ),
    ]
