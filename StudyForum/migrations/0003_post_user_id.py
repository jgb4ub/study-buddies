# Generated by Django 3.0.6 on 2020-11-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0002_auto_20201119_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
