# Generated by Django 4.1 on 2022-09-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0023_alter_languages_level_alter_skills_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languages',
            name='level',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='skills',
            name='level',
            field=models.CharField(max_length=2),
        ),
    ]
