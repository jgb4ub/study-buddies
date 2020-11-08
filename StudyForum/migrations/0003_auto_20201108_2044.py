# Generated by Django 3.1.1 on 2020-11-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0002_remove_post_postid'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=20)),
                ('classNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='classes',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='userid',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='default name', max_length=12),
        ),
    ]
