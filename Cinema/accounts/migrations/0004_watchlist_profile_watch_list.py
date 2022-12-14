# Generated by Django 4.1.3 on 2022-11-23 14:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_fav_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('movie_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='watch_list',
            field=models.ManyToManyField(to='accounts.watchlist'),
        ),
    ]
