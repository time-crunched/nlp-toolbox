# Generated by Django 2.0.5 on 2018-06-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sum_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryRes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='file_upload',
            name='file',
            field=models.FileField(upload_to='summary_files/'),
        ),
    ]
