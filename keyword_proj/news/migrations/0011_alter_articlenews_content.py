# Generated by Django 3.2.6 on 2022-05-21 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_articlenews_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlenews',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]