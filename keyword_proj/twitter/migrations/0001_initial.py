# Generated by Django 3.2.6 on 2022-05-02 09:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='VietNamTwitterTrend',
            fields=[
                ('link', models.URLField(blank=True, null=True)),
                ('trend_name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorldwideTwitterTrend',
            fields=[
                ('count', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('pos', models.IntegerField(blank=True, null=True)),
                ('trend_name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
