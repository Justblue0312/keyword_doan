# Generated by Django 3.2.6 on 2022-03-21 13:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('shares', models.IntegerField(default=0)),
                ('reaction_count', models.IntegerField(default=0)),
                ('comments', models.IntegerField(blank=True, default=0, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('posted_on', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('post_url', models.URLField(blank=True, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('loves', models.IntegerField(default=0)),
                ('wow', models.IntegerField(default=0)),
                ('sad', models.IntegerField(default=0)),
                ('angry', models.IntegerField(default=0)),
                ('haha', models.IntegerField(default=0)),
                ('cares', models.IntegerField(default=0)),
            ],
        ),
    ]
