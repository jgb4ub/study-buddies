# Generated by Django 3.1.1 on 2020-10-22 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0003_auto_20201022_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postID',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self'), max_length=100),
        ),
    ]
