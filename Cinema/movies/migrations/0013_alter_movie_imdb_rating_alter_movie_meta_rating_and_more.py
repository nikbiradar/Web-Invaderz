# Generated by Django 4.1.3 on 2022-11-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movieimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='meta_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rott_rating',
            field=models.FloatField(null=True),
        ),
    ]
