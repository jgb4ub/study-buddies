# Generated by Django 3.1.1 on 2020-10-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0002_post_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postID',
            field=models.CharField(blank=True, default=1, max_length=100, unique=True),
        ),
    ]
