# Generated by Django 3.2.6 on 2022-06-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ggtrends', '0003_trendhotposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendhotposts',
            name='trend_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
