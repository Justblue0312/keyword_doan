# Generated by Django 3.2.6 on 2022-05-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0003_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]