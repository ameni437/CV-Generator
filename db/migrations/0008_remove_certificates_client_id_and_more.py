# Generated by Django 4.1 on 2022-09-08 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_education_description_education_end_education_start_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificates',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='community',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='education',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='hobbies',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='internships',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='languages',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='Client_id',
        ),
        migrations.RemoveField(
            model_name='training',
            name='Client_id',
        ),
    ]
