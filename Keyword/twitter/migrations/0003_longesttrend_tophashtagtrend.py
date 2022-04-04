# Generated by Django 3.2.6 on 2022-03-29 06:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_worldwidetwittertrend'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongestTrend',
            fields=[
                ('link', models.URLField(blank=True, null=True)),
                ('pos', models.IntegerField(blank=True, null=True)),
                ('trend_name', models.CharField(blank=True, max_length=255, null=True)),
                ('tweets', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopHashtagTrend',
            fields=[
                ('link', models.URLField(blank=True, null=True)),
                ('pos', models.IntegerField(blank=True, null=True)),
                ('trend_name', models.CharField(blank=True, max_length=255, null=True)),
                ('tweets', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
