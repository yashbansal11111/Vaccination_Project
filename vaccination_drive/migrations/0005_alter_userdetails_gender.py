# Generated by Django 4.1.dev20211124163835 on 2021-11-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_drive', '0004_alter_userdetails_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Others')], max_length=10),
        ),
    ]
