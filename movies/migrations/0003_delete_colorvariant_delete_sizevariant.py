# Generated by Django 4.1.3 on 2022-11-15 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_category_category_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ColorVariant',
        ),
        migrations.DeleteModel(
            name='SizeVariant',
        ),
    ]
