# Generated by Django 4.1 on 2022-09-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_skills_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internships',
            name='employer',
            field=models.CharField(default='', max_length=40),
        ),
    ]
