# Generated by Django 3.1.1 on 2020-11-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0003_auto_20201124_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='creator',
            field=models.IntegerField(),
        ),
    ]
