# Generated by Django 3.1.1 on 2020-11-13 04:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='na', max_length=12, unique=True)),
                ('professor', models.CharField(default='na', max_length=30)),
                ('time', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='na', max_length=12)),
                ('course', models.CharField(default='na', max_length=12)),
                ('group_description', models.CharField(default='na', max_length=100)),
                ('creator', models.CharField(default='na', max_length=12)),
                ('phone', models.CharField(default='na', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='na', max_length=12)),
                ('group_id', models.IntegerField()),
                ('member_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_passed_in', models.CharField(max_length=12)),
                ('password_passed_in', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='anonymous', max_length=12)),
                ('recipient', models.CharField(default='anonymous', max_length=12)),
                ('content', models.CharField(default='(empty message)', max_length=250)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='na', max_length=12)),
                ('subject', models.CharField(default='na', max_length=50)),
                ('category', models.CharField(default='na', max_length=20)),
                ('content', models.CharField(default='na', max_length=100)),
                ('course', models.CharField(default='na', max_length=20)),
                ('link', models.CharField(default='na', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveIntegerField()),
                ('message', models.CharField(default='na', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('year', models.CharField(default='third year', max_length=100)),
                ('major', models.CharField(default='computer science', max_length=100)),
                ('courses', models.ManyToManyField(to='StudyForum.Course')),
                ('fives', models.ManyToManyField(related_name='fives', to='StudyForum.Course')),
                ('fours', models.ManyToManyField(related_name='fours', to='StudyForum.Course')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('ones', models.ManyToManyField(related_name='ones', to='StudyForum.Course')),
                ('threes', models.ManyToManyField(related_name='threes', to='StudyForum.Course')),
                ('twos', models.ManyToManyField(related_name='twos', to='StudyForum.Course')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
