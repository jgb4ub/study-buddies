# Generated by Django 3.1.1 on 2020-11-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0005_auto_20201124_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='message',
            field=models.CharField(default='na', max_length=100),
        ),
    ]