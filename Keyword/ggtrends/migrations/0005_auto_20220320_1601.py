# Generated by Django 3.2.6 on 2022-03-20 09:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ggtrends', '0004_delete_googleword'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayTrends',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('trend_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrendPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('body', models.CharField(blank=True, max_length=255, null=True)),
                ('trend_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ggtrends.todaytrends')),
            ],
        ),
        migrations.AddField(
            model_name='todaytrends',
            name='trendpost',
            field=models.ManyToManyField(blank=True, to='ggtrends.TrendPosts'),
        ),
    ]
