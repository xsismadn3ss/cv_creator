# Generated by Django 5.1 on 2024-08-21 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_creator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='user_id',
            new_name='user',
        ),
    ]
