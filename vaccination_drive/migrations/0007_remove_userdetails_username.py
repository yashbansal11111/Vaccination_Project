# Generated by Django 4.1.dev20211124163835 on 2021-11-27 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_drive', '0006_userdetails_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='username',
        ),
    ]