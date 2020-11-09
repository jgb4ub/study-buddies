# Generated by Django 3.0.6 on 2020-11-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyForum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='anonymous', max_length=12)),
                ('recipient', models.CharField(default='anonymous', max_length=12)),
                ('content', models.CharField(default='(empty message)', max_length=250)),
                ('time', models.DateTimeField(verbose_name='Time Sent')),
            ],
        ),
    ]