# Generated by Django 2.0.5 on 2018-05-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_v1', '0004_auto_20180529_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='document',
            name='corpus',
            field=models.CharField(choices=[('/Users/Erik/Documents/Python/NLP/Extraction/Corpus/corpus.mm', 'Eriks .docx dokumenter')], default='/Users/Erik/Documents/Python/NLP/Extraction/Corpus/corpus.mm', max_length=200),
        ),
    ]
