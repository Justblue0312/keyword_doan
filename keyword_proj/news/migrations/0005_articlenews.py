# Generated by Django 3.2.6 on 2022-04-28 16:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_delete_msn_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleNews',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('abstract', models.CharField(blank=True, max_length=10000, null=True)),
                ('url', models.URLField()),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('attribution', models.CharField(blank=True, max_length=255, null=True)),
                ('image_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('image_caption', models.CharField(blank=True, max_length=5000, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('reaction_count', models.IntegerField(default=0)),
                ('angry', models.IntegerField(default=0)),
                ('love', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('surprised', models.IntegerField(default=0)),
                ('thinking', models.IntegerField(default=0)),
                ('sad', models.IntegerField(default=0)),
            ],
        ),
    ]
