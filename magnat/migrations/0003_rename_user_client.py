# Generated by Django 4.2.7 on 2023-11-28 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magnat', '0002_alter_media_media_alter_media_youtube_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Client',
        ),
    ]
