# Generated by Django 3.2.6 on 2022-04-28 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_articlenews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlenews',
            name='angry',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='like',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='love',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='sad',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='surprised',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='thinking',
        ),
    ]