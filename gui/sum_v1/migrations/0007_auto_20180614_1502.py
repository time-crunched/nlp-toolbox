# Generated by Django 2.0.5 on 2018-06-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sum_v1', '0006_auto_20180614_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='file',
            field=models.FileField(blank=True, max_length=500, upload_to='sum_v1/upload'),
        ),
    ]
