# Generated by Django 2.0.5 on 2018-06-14 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sum_v1', '0008_file_upload_word_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_upload',
            name='word_count',
        ),
    ]
