# Generated by Django 3.1.1 on 2020-11-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0002_remove_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='na', max_length=12, unique=True),
        ),
    ]
