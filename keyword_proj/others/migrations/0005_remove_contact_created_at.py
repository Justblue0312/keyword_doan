# Generated by Django 3.2.6 on 2022-05-22 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0004_alter_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
    ]
