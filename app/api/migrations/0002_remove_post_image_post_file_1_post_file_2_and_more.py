# Generated by Django 4.0.4 on 2022-05-24 12:07

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='file_1',
            field=models.ImageField(blank=True, upload_to=api.models.upload_to),
        ),
        migrations.AddField(
            model_name='post',
            name='file_2',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
        migrations.AddField(
            model_name='post',
            name='file_3',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
        migrations.AddField(
            model_name='post',
            name='file_4',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
        migrations.AddField(
            model_name='post',
            name='file_5',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
    ]