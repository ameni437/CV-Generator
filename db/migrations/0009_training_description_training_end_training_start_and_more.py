# Generated by Django 4.1 on 2022-09-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_remove_certificates_client_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='training',
            name='end',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='training',
            name='start',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='training',
            name='town',
            field=models.CharField(default=None, max_length=30),
        ),
    ]